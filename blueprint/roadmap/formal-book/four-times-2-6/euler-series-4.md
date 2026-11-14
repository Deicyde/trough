---
declaration: theorem
origin: cited
lean: euler_series_4
statement: formalized
---

# Euler's series: Proof 4

$$
\sum_{n\ge 1}\frac{1}{n^2} = \frac{\pi^2}{6}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The first trick in this proof is to consider the Gregory–Leibniz series in doubly-infinite form $\sum_{n=-\infty}^\infty \frac{(-1)^n}{2n+1}$. As for negative $n = -k < 0$ we get the same terms as for $n = k-1 \ge 0$, since $\frac{(-1)^{-k}}{2(-k)+1} = \frac{(-1)^k}{-(2k-1)} = \frac{(-1)^{k-1}}{2(k-1)+1}$, we infer that $\sum_{n=-N}^N \frac{(-1)^n}{2n+1}$ converges to $\pi/2$ with $N \to \infty$, and thus the square of this sum converges to $\pi^2/4$. You may write this as

$$
\lim_{N \to \infty} \sum_{m,n=-N}^N \frac{(-1)^m}{2m+1} \frac{(-1)^n}{2n+1} = \frac{\pi^2}{4}.
$$

The double sum may be interpreted as the sum of all entries of a square matrix of size $(2N+1) \times (2N+1)$, and we know that for $N \to \infty$ this sum of all entries tends to $\pi^2/4$. We want to know, however, that the sum of only the *diagonal* entries, for $m=n$, also tends to $\pi^2/4$,

$$
\lim_{N \to \infty} \sum_{n=-N}^N \frac{1}{(2n+1)^2} = \frac{\pi^2}{4},
$$

because then $\sum_{n=0}^\infty \frac{1}{(2n+1)^2} = \pi^2/8$ will follow, and this, as we know, is equivalent to Euler's theorem. So let's show that the sum of all off-diagonal terms tends to $0$! We write $\delta_N$ for this sum, and use a prime to denote that the diagonal terms with $m=n$ are deleted, so

$$
\begin{aligned}
\delta_N &= \sideset{}{'}\sum_{m,n=-N}^N \frac{(-1)^{m+n}}{(2m+1)(2n+1)} \\
&= \sideset{}{'}\sum_{m,n=-N}^N (-1)^{m+n} \left(\frac{1}{2m-2n}\frac{1}{2m+1} - \frac{1}{2m-2n}\frac{1}{2n+1}\right) \\
&= \sideset{}{'}\sum_{m,n=-N}^N (-1)^{m+n} \left(\frac{1}{2m-2n}\frac{1}{2m+1} - \frac{1}{2n-2m}\frac{1}{2m+1}\right) \\
&= \sideset{}{'}\sum_{m,n=-N}^N (-1)^{m+n} \frac{1}{m-n} \frac{1}{2m+1} \\
&= \sum_{m=-N}^N \frac{1}{2m+1} \left(\sideset{}{'}\sum_{n=-N}^N \frac{(-1)^{m-n}}{m-n}\right).
\end{aligned}
$$

We only need to show that the terms

$$
c_{m,N} := \sideset{}{'}\sum_{n=-N}^N \frac{(-1)^{m-n}}{m-n}
$$

are small enough in absolute value. What do we know about them? It is easy to see that $c_{-m,N} = -c_{m,N}$, so in particular $c_{0,N} = 0$. Thus we may assume that $m > 0$, and note that the summands for $n = m+k$ and $n = m-k$ cancel as long as they are in the range between $-N$ and $N$, that is, for $1 \le k \le N-m$. Thus $c_{m,N}$ equals the alternating sum of fractions of decreasing size given by the remaining terms, where the largest one occurs for $n = m-(N-m)-1 = 2m-N-1$, that is $m-n = N-m+1$. Hence

$$
c_{m,N} = (-1)^{N-m+1} \left( \frac{1}{N-m+1} - \frac{1}{N-m+2} \pm \dots \pm \frac{1}{m+N} \right),
$$

which implies that

$$
|c_{m,N}| \le \frac{1}{N-m+1}.
$$

This finally yields

$$
\begin{aligned}
|\delta_N| &\le \sum_{m=-N}^N \left|\frac{1}{2m+1}\right| |c_{m,N}| \le \sum_{m=-N}^N \frac{1}{2|m|-1} |c_{m,N}| \\
&\le 2 \sum_{m=1}^N \frac{1}{m} |c_{m,N}| \le 2 \sum_{m=1}^N \frac{1}{m} \frac{1}{N-m+1} \\
&= 2 \sum_{m=1}^N \frac{1}{N+1} \left( \frac{1}{m} + \frac{1}{N-m+1} \right) \\
&= 2 \frac{1}{N+1} (H_N + H_N) < 4 \frac{\log N + 1}{N+1},
\end{aligned}
$$

and this goes to $0$ as $N$ goes to infinity.

## Lean

Stated as [`euler_series_4`](https://mo271.github.io/FormalBook/docs/find/#doc/euler_series_4); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter09.tex, line 189](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter09.tex#L189)
