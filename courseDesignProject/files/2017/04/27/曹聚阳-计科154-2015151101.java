//package cn.edu.dlnu;
import java.util.*;
import java.sql.*;
public class test {
    public Connection connDB() throws SQLException, ClassNotFoundException {
        String drivers = "com.mysql.jdbc.Driver";
        String url = "jdbc:mysql://localhost:3306/test?useSSL=false";
        String user = "root";
        String passwd = "password";
        Connection conn;
        Class.forName(drivers);
        conn = DriverManager.getConnection(url, user, passwd);
        return conn;
    }
    public Map<String, String> input(String[] keys) {
        Scanner in = new Scanner(System.in);
        Map<String, String> stu = new HashMap<String, String>();
        for (String key : keys) {
            stu.put(key, in.nextLine());
        }
        return stu;
    }
    public int execSql(Connection conn, String sql, Map<String, String> tab) throws SQLException {
        PreparedStatement pstmt = conn.prepareStatement(sql);
        int i = 1;
        for (String value : tab.values()) {
            pstmt.setString(i, value);
            i++;
        }
        return pstmt.executeUpdate();
    }
    public void display(ResultSet rs) throws SQLException {
        while (rs.next()) {
            for (int i = 1; i <= rs.getMetaData().getColumnCount(); i++) {
                System.out.print(rs.getString(i) + "    ");
            }
            System.out.print("\n");
        }
    }
    public static void main(String args[]) throws SQLException, ClassNotFoundException {
        test ob = new test();
        Scanner in = new Scanner(System.in);
        Connection conn = ob.connDB();
        String sql = "";

        while (true) {
            System.out.println("1--信息输入功能\n2--信息修改功能\n3--数据删除功能\n4--信息查询功能");
            switch (in.nextInt()) {
            case 1:
                System.out.println("1--输入学生信息\n2--输入课程信息\n3--输入成绩信息");
                switch (in.nextInt()) {
                case 1:
                    System.out.println("输入学生信息:");
                    ob.execSql(conn, "INSERT INTO S(sno, sname, sex, age) VALUES(?,?,?,?)", ob.input(new String[] {"sno", "sname", "sex", "age"}));
                    break;
                case 2:
                    System.out.println("输入课程信息:");
                    ob.execSql(conn, "INSERT INTO C(cno, cname, credit) VALUES(?,?,?)", ob.input(new String[] {"cno", "cname", "credit"}));
                    break;
                case 3:
                    System.out.println("输入成绩信息:");
                    ob.execSql(conn, "INSERT INTO SC(sno,cno,grade) VALUES(?,?,?)", ob.input(new String[] {"sno", "cno", "grade"}));
                    break;
                default:
                    System.out.println("Error");
                }
                break;
            case 2:
                System.out.println("1--按学号修改学生信息\n2--按课程号修改课程信息\n3--按学号和课程号修改成绩信息");
                switch (in.nextInt()) {
                case 1:
                    System.out.println("输入学号和修改后的学生信息：");
                    sql = "UPDATE S SET sname=?, sex=?, age=? WHERE sno='" + in.next() + "'";
                    ob.execSql(conn, sql, ob.input(new String[] {"sname", "sex", "age"}));
                    break;
                case 2:
                    System.out.println("输入课程号和修改后的课程信息：");
                    sql = "UPDATE C SET cname=?, credit=? WHERE cno='" + in.next() + "'";
                    ob.execSql(conn, sql, ob.input(new String[] {"cname", "credit"}));
                    break;
                case 3:
                    System.out.println("输入学生号、课程号、成绩：");
                    sql = "UPDATE SC SET grade=? WHERE sno='" + in.next() + "' AND cno='" + in.next() + "'";
                    ob.execSql(conn, sql, ob.input(new String[] {"grade"}));
                    break;
                default:
                    System.out.println("Error");
                }
                break;
            case 3:
                System.out.println("1--按学号删除学生信息\n2--按课程号删除课程信息\n3--按学号和课程号删除成绩信息");
                conn.prepareStatement("SET FOREIGN_KEY_CHECKS = 0").execute();
                switch (in.nextInt()) {
                case 1:
                    System.out.println("输入学号：");
                    ob.execSql(conn, "DELETE FROM S WHERE sno=?", ob.input(new String[] {"sno"}));
                    break;
                case 2:
                    System.out.println("输入课程号：");
                    ob.execSql(conn, "DELETE FROM C WHERE cno=?", ob.input(new String[] {"cno"}));
                    break;
                case 3:
                    System.out.println("输入学生号、课程号：");
                    ob.execSql(conn, "DELETE FROM SC WHERE sno=? AND cno=?", ob.input(new String[] {"sno", "cno"}));
                    break;
                default:
                    System.out.println("Error");
                }
                break;
            case 4:
                System.out.println("1--查询学生表的全部信息\n2--按学号查询学生的基本信息\n3--查询某学生选某课程的成绩情况\n4--查询某学生所得学分明细及总学分\n5--按学生的总成绩排榜（降序）\n6--查询每个系对应的学生人数");
                switch (in.nextInt()) {
                case 1:
                    ob.display(conn.prepareStatement("SELECT * FROM S").executeQuery());
                    break;
                case 2:
                    System.out.println("输入学号：");
                    ob.display(conn.prepareStatement("SELECT * FROM S WHERE sno='" + in.nextInt() + "'").executeQuery());
                    break;
                case 3:
                    System.out.println("输入学号和课程号：");
                    ob.display(conn.prepareStatement("SELECT * FROM SC WHERE sno='" + in.nextInt() + "' AND cno='" + in.nextInt() + "'").executeQuery());
                    break;
                case 4:
                    System.out.println("输入学号：");
                    ob.display(conn.prepareStatement("SELECT * FROM SC, C WHERE sno='" + in.nextInt() + "'").executeQuery());
                    break;
                case 5:
                    ob.display(conn.prepareStatement("SELECT sno, SUM(grade) FROM sc GROUP BY sno ORDER BY SUM(grade) DESC").executeQuery());
                    break;
                case 6:
                    ob.display(conn.prepareStatement("SELECT dept, COUNT(dept) FROM s GROUP BY dept").executeQuery());
                    break;
                default:
                    System.out.println("Error");
                }
                break;
            default:
                System.out.println("Error");
            }
        }
    }
}