/*
https://github.com/chocoteam/choco-solver
https://choco-solver.readthedocs.io/en/latest/1_overview.html#example
http://www.choco-solver.org/
<dependency>
            <groupId>org.choco-solver</groupId>
            <artifactId>choco-solver</artifactId>
            <version>4.10.2</version>
        </dependency>

*/
public class  Test  {
    public static void test1() {
        // 1. Create a Model
        long now = new Date().getTime();
        Model model = new Model("my first problem");
        // 2. Create variables
        IntVar x1 = model.intVar("X1", 26, 44);
        IntVar x2 = model.intVar("X2", 19, 33);
        IntVar x3 = model.intVar("X3", 26, 44);
        IntVar x31 = model.intScaleView(x3 ,-1);
        IntVar x4 = model.intVar("X4", 19, 33);
        IntVar x41 = model.intScaleView(x4 ,-1);
        IntVar x5 = model.intVar("X5", 26, 46);
        IntVar x6 = model.intVar("X6", 16, 28);
        IntVar x7 = model.intVar("X7", 26, 46);
        IntVar x71 = model.intScaleView(x7 ,-1);
        IntVar x8 = model.intVar("X8", 16, 28);
        IntVar x81 = model.intScaleView(x8 ,-1);

        IntVar[] c1 = new IntVar[4];
        c1[0] = x1;c1[1] = x2;c1[2] = x31;c1[3] = x41;
        model.sum(c1, "=", 0).post();

        IntVar[] c2 = new IntVar[4];
        c2[0] = x5;c2[1] = x6;c2[2] = x71;c2[3] = x81;
        model.sum(c2, "=", 0).post();

        IntVar[] c3 = new IntVar[4];
        c3[0] = x1;c3[1] = x2;c3[2] = x5;c3[3] = x6;
        model.sum(c3, "=", 118).post();


        model.ifThen(
                model.arithm(x1, "-", x3, ">", 0),
                model.arithm(x1, "-", x3, ">", 2)
        );
        model.ifThen(
                model.arithm(x1, "-", x3, "<", 0),
                model.arithm(x1, "-", x3, "<", -2)
        );
        model.ifThen(
                model.arithm(x5, "-", x7, ">", 0),
                model.arithm(x5, "-", x7, ">", 2)
        );
        model.ifThen(
                model.arithm(x5, "-", x7, "<", 0),
                model.arithm(x5, "-", x7, "<", -2)
        );

        System.out.println(model.toString());
        int i=0;
        while (model.getSolver().solve()) {i++;
//            System.out.println(x1 + " " + x2 + " " + x3 + " " + x4 + " "
//            + x5 + " " + x6 + " " + x7 + " " + x8); // Prints X = 2
        }
        System.out.println(new Date().getTime() - now);
        System.out.println(i);
        System.exit(0);
    }
    public static void test() {

        // 1. Create a Model
        long now = new Date().getTime();
        Model model = new Model("my first problem");
        // 2. Create variables
        IntVar x1 = model.intVar("X1", 14, 139);
        IntVar x2 = model.intVar("X2", 14, 139);
        IntVar x3 = model.intVar("X3", 14, 139);
        IntVar x31 = model.intScaleView(x3 ,-1);
        IntVar x4 = model.intVar("X4", 14, 139);
        IntVar x41 = model.intScaleView(x4 ,-1);
        IntVar x5 = model.intVar("X5", 8, 139);
        IntVar x6 = model.intVar("X6", 8, 139);
        IntVar x61 = model.intScaleView(x6 ,-1);
        IntVar x7 = model.intVar("X7", 8, 139);
        IntVar x71 = model.intScaleView(x7 ,-1);
        IntVar x8 = model.intVar("X8", 8, 139);
        IntVar x81 = model.intScaleView(x8 ,-1);

        IntVar[] c1 = new IntVar[4];
        c1[0] = x1;c1[1] = x2;c1[2] = x31;c1[3] = x41;
        model.sum(c1, "=", 0).post();

        IntVar[] c2 = new IntVar[2];
        c2[0] = x5;c2[1] = x61;
        model.sum(c2, "=", 0).post();

        IntVar[] c3 = new IntVar[2];
        c3[0] = x5;c3[1] = x71;
        model.sum(c3, "=", 0).post();

        IntVar[] c4 = new IntVar[2];
        c4[0] = x5;c4[1] = x81;
        model.sum(c4, "=", 0).post();

        model.arithm(x5, "=", 42).post();
        model.arithm(x6, "=", 42).post();
        model.arithm(x7, "=", 42).post();
        model.arithm(x8, "=", 42).post();

        IntVar[] c10 = new IntVar[3];
        c10[0] = x1;c10[1] = x2;c10[2] = x5;
        model.sum(c10, "=", 139).post();

        model.ifThen(
                model.arithm(x1, "-", x3, ">", 0),
                model.arithm(x1, "-", x3, ">", 2)
        );
        model.ifThen(
                model.arithm(x1, "-", x3, "<", 0),
                model.arithm(x1, "-", x3, "<", -2)
        );

        System.out.println(model.toString());
        int i=0;
        while (model.getSolver().solve()) {i++;
//            System.out.println(x1 + " " + x2 + " " + x3 + " " + x4 + " "
//            + x5 + " " + x6 + " " + x7 + " " + x8); // Prints X = 2
        }
        System.out.println(new Date().getTime() - now);
        System.out.println(i);
        System.exit(0);
    }
    public static void main(String[] args) {
        test1();

        // 1. Create a Model
        long now = new Date().getTime();
        Model model = new Model("my first problem");
        // 2. Create variables
        IntVar x1 = model.intVar("X1", 29, 37);
        IntVar x2 = model.intVar("X2", 16, 20);
        IntVar x3 = model.intVar("X3", 46, 62);
        IntVar x31 = model.intOffsetView(x3, -3);
        IntVar x4 = model.intVar("X4", 24, 32);// x in [0,5]
        IntVar x41 = model.intOffsetView(model.intScaleView(x4, -1), 79);
        //IntVar y = model.intVar("Y", new int[]{2, 3, 8});   // y in {2, 3, 8}
        // 3. Post constraints

        model.arithm(x1, "+", x2, "+", x31).post(); // x + y < 5
        model.arithm(x1, "+", x2, "=", x41).post(); // x + y < 5

        //model.times(x,y,4).post();              // x * y = 4
        // 4. Solve the problem

       // model.getSolver().showSolutions();
        //model.getSolver().showStatistics();
        model.ifThen(
                model.arithm(x1, "-", x2, ">", 0),
                model.arithm(x1, "-", x2, ">", 15)
        );
        model.ifThen(
                model.arithm(x1, "-", x2, "<", 0),
                model.arithm(x1, "-", x2, "<", -15)
        );
        System.out.println(model.toString());
        while (model.getSolver().solve()) {
            System.out.println(x1 + " " + x2 + " " + x3 + " " + x4); // Prints X = 2
        }
System.out.println(new Date().getTime() - now);
        System.exit(0);


    }
}
