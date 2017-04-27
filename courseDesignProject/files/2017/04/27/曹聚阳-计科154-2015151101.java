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
            System.out.println("1--��Ϣ���빦��\n2--��Ϣ�޸Ĺ���\n3--����ɾ������\n4--��Ϣ��ѯ����");
            switch (in.nextInt()) {
            case 1:
                System.out.println("1--����ѧ����Ϣ\n2--����γ���Ϣ\n3--����ɼ���Ϣ");
                switch (in.nextInt()) {
                case 1:
                    System.out.println("����ѧ����Ϣ:");
                    ob.execSql(conn, "INSERT INTO S(sno, sname, sex, age) VALUES(?,?,?,?)", ob.input(new String[] {"sno", "sname", "sex", "age"}));
                    break;
                case 2:
                    System.out.println("����γ���Ϣ:");
                    ob.execSql(conn, "INSERT INTO C(cno, cname, credit) VALUES(?,?,?)", ob.input(new String[] {"cno", "cname", "credit"}));
                    break;
                case 3:
                    System.out.println("����ɼ���Ϣ:");
                    ob.execSql(conn, "INSERT INTO SC(sno,cno,grade) VALUES(?,?,?)", ob.input(new String[] {"sno", "cno", "grade"}));
                    break;
                default:
                    System.out.println("Error");
                }
                break;
            case 2:
                System.out.println("1--��ѧ���޸�ѧ����Ϣ\n2--���γ̺��޸Ŀγ���Ϣ\n3--��ѧ�źͿγ̺��޸ĳɼ���Ϣ");
                switch (in.nextInt()) {
                case 1:
                    System.out.println("����ѧ�ź��޸ĺ��ѧ����Ϣ��");
                    sql = "UPDATE S SET sname=?, sex=?, age=? WHERE sno='" + in.next() + "'";
                    ob.execSql(conn, sql, ob.input(new String[] {"sname", "sex", "age"}));
                    break;
                case 2:
                    System.out.println("����γ̺ź��޸ĺ�Ŀγ���Ϣ��");
                    sql = "UPDATE C SET cname=?, credit=? WHERE cno='" + in.next() + "'";
                    ob.execSql(conn, sql, ob.input(new String[] {"cname", "credit"}));
                    break;
                case 3:
                    System.out.println("����ѧ���š��γ̺š��ɼ���");
                    sql = "UPDATE SC SET grade=? WHERE sno='" + in.next() + "' AND cno='" + in.next() + "'";
                    ob.execSql(conn, sql, ob.input(new String[] {"grade"}));
                    break;
                default:
                    System.out.println("Error");
                }
                break;
            case 3:
                System.out.println("1--��ѧ��ɾ��ѧ����Ϣ\n2--���γ̺�ɾ���γ���Ϣ\n3--��ѧ�źͿγ̺�ɾ���ɼ���Ϣ");
                conn.prepareStatement("SET FOREIGN_KEY_CHECKS = 0").execute();
                switch (in.nextInt()) {
                case 1:
                    System.out.println("����ѧ�ţ�");
                    ob.execSql(conn, "DELETE FROM S WHERE sno=?", ob.input(new String[] {"sno"}));
                    break;
                case 2:
                    System.out.println("����γ̺ţ�");
                    ob.execSql(conn, "DELETE FROM C WHERE cno=?", ob.input(new String[] {"cno"}));
                    break;
                case 3:
                    System.out.println("����ѧ���š��γ̺ţ�");
                    ob.execSql(conn, "DELETE FROM SC WHERE sno=? AND cno=?", ob.input(new String[] {"sno", "cno"}));
                    break;
                default:
                    System.out.println("Error");
                }
                break;
            case 4:
                System.out.println("1--��ѯѧ�����ȫ����Ϣ\n2--��ѧ�Ų�ѯѧ���Ļ�����Ϣ\n3--��ѯĳѧ��ѡĳ�γ̵ĳɼ����\n4--��ѯĳѧ������ѧ����ϸ����ѧ��\n5--��ѧ�����ܳɼ��Ű񣨽���\n6--��ѯÿ��ϵ��Ӧ��ѧ������");
                switch (in.nextInt()) {
                case 1:
                    ob.display(conn.prepareStatement("SELECT * FROM S").executeQuery());
                    break;
                case 2:
                    System.out.println("����ѧ�ţ�");
                    ob.display(conn.prepareStatement("SELECT * FROM S WHERE sno='" + in.nextInt() + "'").executeQuery());
                    break;
                case 3:
                    System.out.println("����ѧ�źͿγ̺ţ�");
                    ob.display(conn.prepareStatement("SELECT * FROM SC WHERE sno='" + in.nextInt() + "' AND cno='" + in.nextInt() + "'").executeQuery());
                    break;
                case 4:
                    System.out.println("����ѧ�ţ�");
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