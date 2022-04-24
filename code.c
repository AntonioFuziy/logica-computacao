{
    i = 1;
    n = 5;
    while ((i < n) || (i == n)) {
        if (x > y)
            y = y + 1;
            printf("if");
        else if (x < y)
            x = x + 1;
            printf("elif");
        else
            x = x + i;
            printf("else");
        i = i + 1;
    }
}