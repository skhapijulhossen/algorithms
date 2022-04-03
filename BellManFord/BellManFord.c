#include <stdio.h>
#include <stdlib.h>

#define INF 9999;

struct Edge
{
    int u, v, w;
};

struct Graph
{
    int vertices, edges;
    struct Edge *edge;
};

struct Graph *initialize_Graph()
{
    int vertices, edges;
    struct Graph *G = (struct Graph *)malloc(sizeof(struct Graph));
    printf("\n No. Of vertices: ");
    scanf("%d", &vertices);
    printf("\n No. Of Edges: ");
    scanf("%d", &edges);
    G->vertices = vertices;
    G->edges = edges;
    G->edge = (struct Edge *)malloc(G->edges * sizeof(struct Edge));
    for (int e = 0; e < edges; e++)
    {
        printf("\n Enter Edge %d info U V W: ", e);
        scanf("%d%d%d", &G->edge[e].u, &G->edge[e].v, &G->edge[e].w);
    }
    for (int e = 0; e < edges; e++)
    {
        printf("\n Enter Edge %d info U=%d V=%d W=%d: ", e, G->edge[e].u, G->edge[e].v, G->edge[e].w);
    }
    return G;
}

int BellManFord(struct Graph *G, int source)
{
    int distance[G->vertices], predesessor[G->edges];
    for (int d = 0; d < G->vertices; d++)
    {
        distance[d] = INF;
        predesessor[d] = -1;
    }
    distance[source] = 0;

    for (int e = 0; e < G->edges - 1; e++)
    {
        if (distance[G->edge[e].v] > (distance[G->edge[e].u] + G->edge[e].w))
        {
            distance[G->edge[e].v] = distance[G->edge[e].u] + G->edge[e].w;
            predesessor[G->edge[e].v] = G->edge[e].u;
        }
    }

    for (int e = 0; e < G->edges - 1; e++)
    {
        if (distance[G->edge[e].v] > (distance[G->edge[e].u] + G->edge[e].w))
        {
            return -1;
        }
    }
    printf("Distance Array D: | ");
    for (int v = 0; v < G->vertices; v++)
    {
        printf(" %d |", distance[v]);
    }
    printf("\t Predecessor Array: | ");
    for (int p = 0; p < G->vertices; p++)
    {
        printf(" %d |", predesessor[p]);
    }
    return 1;
}

// Main Function
int main()
{
    struct Graph *g = initialize_Graph();
    BellManFord(g, 0);
    return 0;
}