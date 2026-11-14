---
declaration: lemma
origin: cited
lean: MIPRE.Cost.efficient_fixed_point, MIPRE.Cost.kleeneFix, MIPRE.Cost.kleeneFix_runs_of
statement: formalized
proof: formalized
---

# Efficient Kleene recursion theorem

For every polynomial-time computable $f : \{0,1\}^* \to \{0,1\}^*$ there is a program $e$ with $\phi_e = \phi_{f(e)}$ and the runtime of $e$ polynomially bounded in terms of that of $f(e)$. (This is the direction used by Lemma [Recursive compression](lem-recursive-compression.md); (MNY) states the runtimes as polynomially equivalent, and the converse direction would require a simulator that is never faster than the simulated program.)

## Depends on

- [Efficient universal Turing machine](lem-universal-tm.md)
- [Efficient s-m-n](lem-smn.md)

## Proof

The classical construction. Let $G$ be the program that on input $(x, v)$ computes $s(x, x)$ (Lemma [Efficient s-m-n](lem-smn.md)), applies $f$ to it, and runs the resulting program on $v$ through the universal machine (Lemma [Efficient universal Turing machine](lem-universal-tm.md)); put $e = s(G, G)$. Then $e$ on $v$ is $G$ on $(G, v)$, which runs $f(s(G, G)) = f(e)$ on $v$: the two programs halt on the same inputs with the same results (the backward direction inverts the run of $G$ step by step and uses that the universal machine halts only if the simulated program does), and a run of $f(e)$ of time $t$ gives a run of $e$ within $p(\left\vert {v} \right\vert, t)$, where $p$ is the universal machine's overhead polynomial shifted by the fixed size of $f(e)$, plus a linear term for the copies of the input and a constant for the fixed computation of $f(e)$.

## Lean

Formalized as [`MIPRE.Cost.efficient_fixed_point`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.efficient_fixed_point), [`MIPRE.Cost.kleeneFix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.kleeneFix), [`MIPRE.Cost.kleeneFix_runs_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.kleeneFix_runs_of).

## Sources

- [MIP* = RE blueprint: content/04_computability.tex, line 176](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/04_computability.tex#L176)
