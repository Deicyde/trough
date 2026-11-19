---
declaration: lemma
origin: cited
lean: MIPRE.Cost.Prog.pushProg_runs_le, MIPRE.Tailored.parseDIn, MIPRE.Tailored.parseDIn_encode, MIPRE.Tailored.canonProgT, MIPRE.Tailored.canonProgT_wellScoped, MIPRE.Tailored.canonProgT_runs_iff, MIPRE.Tailored.step_runs, MIPRE.Tailored.canonBound, MIPRE.Tailored.canonProgT_halts, MIPRE.Tailored.canonPoly, MIPRE.Tailored.canonBound_le, MIPRE.Tailored.dom_canonBound, MIPRE.Tailored.canonProgT_timeBound, MIPRE.Tailored.esize_canonProgT
statement: formalized
proof: formalized
---

# The running time of the canonical decider

Put a total parse of the input $(n, x, y, a, b)$ in front of the canonical decider; on encoded inputs it is the identity, so the decider accepts what it accepted. There are constants $c, m, e$ such that, when $L$ and $LP$ halt within $T(|d| + 1)^k$ on every input $(n, d)$, the decider halts within $c\,(T + 10^k + |n| + 1)^m (|d| + 1)^{e(k+1)}$ on every input $(n, d)$, malformed ones included. Its description is $4|L| + |LP|$ plus a constant.

## Depends on

- [The canonical decider, as a program; II:1757–1787](../part-01/def-canonical-decider.md)

## Proof

Every call reads only components of the parsed input: $L$ on $(n, x, \kappa)$ and $(n, y, \kappa)$, $LP$ on $(n, x, y, a^R, b^R)$, each of size linear in $|d|$, so each costs at most $T\,(20|d| + 20)^k$, and so does its output. The polynomial-time steps between them run on states made of the input and these outputs, so their costs are polynomials in $T(20|d|+20)^k$ and the parse's cost, a polynomial in $|n| + |d|$. The domination tools of the repeated programs turn the sum into the stated shape.

## Lean

Formalized as [`MIPRE.Cost.Prog.pushProg_runs_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Prog.pushProg_runs_le), [`MIPRE.Tailored.parseDIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.parseDIn), [`MIPRE.Tailored.parseDIn_encode`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.parseDIn_encode), [`MIPRE.Tailored.canonProgT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.canonProgT), [`MIPRE.Tailored.canonProgT_wellScoped`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.canonProgT_wellScoped), [`MIPRE.Tailored.canonProgT_runs_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.canonProgT_runs_iff), [`MIPRE.Tailored.step_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.step_runs), [`MIPRE.Tailored.canonBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.canonBound), [`MIPRE.Tailored.canonProgT_halts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.canonProgT_halts), [`MIPRE.Tailored.canonPoly`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.canonPoly), [`MIPRE.Tailored.canonBound_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.canonBound_le), [`MIPRE.Tailored.dom_canonBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.dom_canonBound), [`MIPRE.Tailored.canonProgT_timeBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.canonProgT_timeBound), [`MIPRE.Tailored.esize_canonProgT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.esize_canonProgT).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1640](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1640)
