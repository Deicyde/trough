---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.RepProg.repLen_timeBound, MIPRE.Tailored.RepProg.repLp_timeBound, MIPRE.Tailored.RepProg.repLen_lenBound
statement: formalized
proof: formalized
---

# Running times of the repeated programs

With the input sampler within $T_S \cdot (|d| + 1)^K$ and the input programs within $T_D \cdot (|d| + 1)^K$ at index $n$, the repeated programs halt on every input within $c\,(W + 1)^m (|d| + 1)^{e (K + 1)}$, for a bound $W$ on $T_S$, $T_D$, $\lambda$, $\tau$, $n$, $k(n)$, $s(n)$, $10^K$ and the descriptions of the input programs, and constants $c, m, e$; and the repeated calculator's lengths are at most $k(n)$ times the input's.

## Depends on

- [The repeated programs](def-tailored-rep-programs.md)

## Proof depends on

- [The repeated programs meet the specification](lem-tailored-rep-programs.md)

## Proof

Every stage between the calls is a polynomial-time function of an input of size polynomial in $W$ and $|d|$. Every query to an input program is of size linear in $|d|$, so a call costs at most the universal machine's overhead at $T_D (c|d|)^K \le W^{j} |d|^K$, using $10^K \le W$, and there are at most $4k(n)$ calls.

## Lean

Formalized as [`MIPRE.Tailored.RepProg.repLen_timeBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.RepProg.repLen_timeBound), [`MIPRE.Tailored.RepProg.repLp_timeBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.RepProg.repLp_timeBound), [`MIPRE.Tailored.RepProg.repLen_lenBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.RepProg.repLen_lenBound).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1291](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1291)
