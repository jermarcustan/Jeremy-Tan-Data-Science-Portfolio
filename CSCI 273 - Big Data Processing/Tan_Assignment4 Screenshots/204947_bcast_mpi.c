#include "mpi.h"
#include <math.h>
#include <stdio.h>

int main(argc,argv)
int argc;
char *argv[];
{
    int done = 0, myid, numprocs, i;
    long n;
    double PI25DT = 3.141592653589793238462643;
    double mypi, pi, h, sum, x;
    double x1, x2, fx1, fx2;

    n=10000000;

    MPI_Init(&argc,&argv);
    MPI_Comm_size(MPI_COMM_WORLD,&numprocs);
    MPI_Comm_rank(MPI_COMM_WORLD,&myid);
    while (!done)
    {
        MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);
        if (n == 0) break;

        h   = 1.0 / (double) n;
        sum = 0.0;
        for (i = myid; i <= n; i += numprocs) {
            x1 = h * ((double)i);
            x2 = h * ((double)i + 1);
            fx1 = 4.0 / (1.0 + (x1 * x1));
            fx2 = 4.0 / (1.0 + (x2 * x2));
            sum += fx1 + fx2;
        }
        mypi = 0.5 * h * sum;

        MPI_Reduce(&mypi, &pi, 1, MPI_DOUBLE, MPI_SUM, 0,
                   MPI_COMM_WORLD);

        if (myid == 0)
            printf("pi is approximately %.16f, Error is %.16f\n",
                   pi, fabs(pi - PI25DT));
            done = 1;
    }
    MPI_Finalize();
    return 0;
}
