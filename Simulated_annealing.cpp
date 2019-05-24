#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <stdio.h>
#include <time.h>
#include <math.h>

#define N     30      //城市数量
#define T     3000    //初始温度
#define EPS   1e-8    //终止温度
#define DELTA 0.98    //温度衰减率

#define LIMIT 1000   //概率选择上限
#define OLOOP 20    //外循环次数
#define ILOOP 100   //内循环次数

using namespace std;

//定义路线结构体
struct Path
{
    int citys[N];
    double len;
};

//定义城市点坐标
struct Point
{
    double x, y;
};

Path bestPath;        //记录最优路径
Point p[N];       //每个城市的坐标
double w[N][N];   //两两城市之间路径长度
int nCase;        //测试次数

double dist(Point A, Point B)
{
    return sqrt((A.x - B.x) * (A.x - B.x) + (A.y - B.y) * (A.y - B.y));
}

void GetDist(Point p[], int n)
{
    for(int i = 0; i < n; i++)
        for(int j = i + 1; j < n; j++)
            w[i][j] = w[j][i] = dist(p[i], p[j]);
}

void Input(Point p[], int &n)
{
    scanf("%d", &n);
    for(int i = 0; i < n; i++)
        scanf("%lf %lf", &p[i].x, &p[i].y);
}

void Init(int n)
{
    nCase = 0;
    bestPath.len = 0;
    for(int i = 0; i < n; i++)
    {
        bestPath.citys[i] = i;
        if(i != n - 1)
        {
            printf("%d--->", i);
            bestPath.len += w[i][i + 1];
        }
        else
            printf("%d\n", i);
    }
    printf("\nInit path length is : %.3lf\n", bestPath.len);
    printf("-----------------------------------\n\n");
}

void Print(Path t, int n)
{
    printf("Path is : ");
    for(int i = 0; i < n; i++)
    {
        if(i != n - 1)
            printf("%d-->", t.citys[i]);
        else
            printf("%d\n", t.citys[i]);
    }
    printf("\nThe path length is : %.3lf\n", t.len);
    printf("-----------------------------------\n\n");
}

Path GetNext(Path p, int n)
{
    Path ans = p;
    int x = (int)(n * (rand() / (RAND_MAX + 1.0)));
    int y = (int)(n * (rand() / (RAND_MAX + 1.0)));
    while(x == y)
    {
        x = (int)(n * (rand() / (RAND_MAX + 1.0)));
        y = (int)(n * (rand() / (RAND_MAX + 1.0)));
    }
    swap(ans.citys[x], ans.citys[y]);
    ans.len = 0;
    for(int i = 0; i < n - 1; i++)
        ans.len += w[ans.citys[i]][ans.citys[i + 1]];
    cout << "nCase = " << nCase << endl;
    Print(ans, n);
    nCase++;
    return ans;
}

void SA(int n)
{
    double t = T;
    srand((unsigned)(time(NULL)));
    Path curPath = bestPath;
    Path newPath = bestPath;
    int P_L = 0;
    int P_F = 0;
    while(1)       //外循环，主要更新参数t，模拟退火过程
    {
        for(int i = 0; i < ILOOP; i++)    //内循环，寻找在一定温度下的最优值
        {
            newPath = GetNext(curPath, n);
            double dE = newPath.len - curPath.len;
            if(dE < 0)   //如果找到更优值，直接更新
            {
                curPath = newPath;
                P_L = 0;
                P_F = 0;
            }
            else
            {
                double rd = rand() / (RAND_MAX + 1.0);
                //如果找到比当前更差的解，以一定概率接受该解，并且这个概率会越来越小
                if(exp(dE / t) > rd && exp(dE / t) < 1)
                    curPath = newPath;
                P_L++;
            }
            if(P_L > LIMIT)
            {
                P_F++;
                break;
            }
        }
        if(curPath.len < bestPath.len)
            bestPath = curPath;
        if(P_F > OLOOP || t < EPS)
            break;
        t *= DELTA;
    }
}

int main(int argc, const char * argv[]) {

    freopen("TSP.data", "r", stdin);
    int n;
    Input(p, n);
    GetDist(p, n);
    Init(n);
    SA(n);
    Print(bestPath, n);
    printf("Total test times is : %d\n", nCase);
    return 0;
}
