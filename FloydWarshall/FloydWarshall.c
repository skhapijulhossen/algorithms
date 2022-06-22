#include <stdio.h>
#include <stdlib.h>

#define INF 999;

int **initialize_Graph(int vertices)
{
    int graph[vertices][vertices];

    for (int u = 0; u < vertices; u++)
    {
        for (int e = 0; e < vertices; e++)
        {
            printf("\n Edge Weight from %d to %d :(if no direct edge enter 999): ", u, e);
            scanf("%d", &graph[u][e]);
        }
    }
    return graph;
}

int showGraph(int **graph, int vertices)
{

    for (int u = 0; u < vertices; u++)
    {

        printf("\nFrom %d: ");
        for (int e = 0; e < vertices; e++)
        {
            printf(" %d |", graph[u][e]);
        }
    }
}

int main()
{
    int vertices, **graph;
    printf("\nNo. Of Vertices: ");
    scanf("%d", &vertices);
    graph = initialize_Graph(vertices);
    showGraph(graph, vertices);
    return 0;
}