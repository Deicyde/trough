# Numbers again

Look at the incidence matrix for $R = C = \{1, 2, \dots, n\}$ and $S = \{(i,j) : i \mid j\}$. The number of $1$'s in column $j$ is precisely the number of divisors of $j$; let us denote this number by $t(j)$. Let us ask how large this number $t(j)$ is on the average when $j$ ranges from $1$ to $n$. Thus, we ask for the quantity

$$
\bar{t}(n) = \frac{1}{n} \sum_{j=1}^{n} t(j).
$$

How large is $\bar{t}(n)$ for arbitrary $n$? At first glance, this seems hopeless. For prime numbers $p$ we have $t(p) = 2$, while for $2^k$ we obtain a large number $t(2^k) = k + 1$. So, $t(n)$ is a wildly jumping function, and we surmise that the same is true for $\bar{t}(n)$. Wrong guess, the opposite is true! Counting in two ways provides an unexpected and simple answer.

- [Average number of divisors](ch28-avg-divisors.md)
