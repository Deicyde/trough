---
declaration: lemma
origin: cited
lean: ZHat.e_not_in_Int
statement: formalized
proof: formalized
---

# ZHat.e_not_in_Int

The element $(e_N)_N$ of $\widehat{\mathbb{Z}}$ is not in $\mathbb{Z}$.

## Depends on

- [ZHat.e](zhat-e.md)

## Proof

First imagine that $e=n$ with $n\in\mathbb{Z}$ and $0\leq n$. In this case, choose $j$ such that $0!+1!+2!+\cdots+j!>n$ and check also that the sum is less than $(j+1)!$. Now set $N=(j+1)!$ and let's compare $e_N$ and $n_N=n$. The trick is that $e_N$ must be $0!+1!+\cdots+j!$ mod $N$, because all the terms beyond this are multiples not just of $(j+1)$ but of $(j+1)!=N$. Thus mod $N$ we have $0\leq n\lt e_N\lt N$ so $n\not=e$.

Now we deal with $n=-t<0$; choose $j$ large such that $(j+1)!-(0!+1!+\cdots+j!)>t$ (possible because the sum is at most $2\times j!$) and then set $N=(j+1)!$ and we have $0 < e_N\lt N-t\lt N$ so we cannot have $e_N=-t$ in $\mathbb{Z}/N\mathbb{Z}$, so again $e\not=n$.

## Lean

Formalized as [`ZHat.e_not_in_Int`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/ZHat.e_not_in_Int).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch05automorphicformexample.tex, line 165](https://github.com/ImperialCollegeLondon/FLT/blob/019805815d7da565ed1e9f427b6fbd0cbc9d00d3/blueprint/src/chapter/ch05automorphicformexample.tex#L165)
