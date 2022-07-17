#include <iostream>

float fractionalKnapsack(float weight[], float profit[], float ratio[], float capacity, int items)
{
    int i = 0;
    float maxprofit = 0.0, part;
    while (weight[i] <= capacity)
    {
        maxprofit = maxprofit + profit[i];
        capacity = capacity - float(weight[i]);
        i++;
    }
    if (i < items)
    {
        part = capacity / weight[i];
        maxprofit = maxprofit + part * profit[i];
    }

    return maxprofit;
}

int main()
{
    int items;
    float capacity;
    std::cout << "Items: ";
    std::cin >> items;
    std::cout<<"\nCapacity: ";
    std::cin>>capacity;
    float profit[items], weight[items];
    float ratio[items];
    for (int item = 0; item < items; item++)
    {
        std::cout << "\nweight profit: ";
        std::cin >> weight[item] >> profit[item];
        ratio[item] = profit[item] / weight[item];
    }

    // sort by ratio
    for (int i = 0; i < items; i++)
    {
        for (int j = i + 1; j < items; j++)
        {
            if (ratio[i] < ratio[j])
            {
                ratio[i] = ratio[i] + ratio[j];
                ratio[j] = ratio[i] - ratio[j];
                ratio[i] = ratio[i] - ratio[j];

                profit[i] = profit[i] + profit[j];
                profit[j] = profit[i] - profit[j];
                profit[i] = profit[i] - profit[j];

                weight[i] = weight[i] + weight[j];
                weight[j] = weight[i] - weight[j];
                weight[i] = weight[i] - weight[j];
            }
        }
    }
    std::cout << "Max Profit: " << fractionalKnapsack(weight, profit, ratio, capacity, items);
    return 0;
}