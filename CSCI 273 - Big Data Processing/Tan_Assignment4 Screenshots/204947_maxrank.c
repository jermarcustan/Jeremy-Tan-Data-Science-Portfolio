#include <stdio.h>
#include <mpi.h>

int main(int argc, char *argv[]) {
    int id = 0;
    int numprocs = 0;
    int sum = 0;
    int total_sum = 0;

    // Initialize MPI
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
    MPI_Comm_rank(MPI_COMM_WORLD, &id);

    // Each process contributes its rank to the sum
    sum = id;

    // Add all ranks at process 0
    MPI_Reduce(&sum, &total_sum, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    // Only process 0 prints the final sum
    if (id == 0) {
        printf("Sum of all ranks is: %d\n", total_sum);
    }

    // Finalize MPI
    MPI_Finalize();
    return 0;
}