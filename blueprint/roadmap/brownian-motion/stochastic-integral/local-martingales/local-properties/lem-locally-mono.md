---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.Locally.mono
---

# locally_mono

If $P \subseteq Q$ then $P_{\mathrm{loc}} \subseteq Q_{\mathrm{loc}}$.

## Depends on

- [Local property](def-locally.md)

## Proof

Let $X \in P_{\mathrm{loc}}$. Then there exists a localizing sequence $(\tau_n)_{n \in \mathbb{N}}$ such that for all $n \in \mathbb{N}$, $X^{\tau_n}\mathbb{I}_{\tau_n > 0} \in P$. Since $P \subseteq Q$, for all $n \in \mathbb{N}$, $X^{\tau_n}\mathbb{I}_{\tau_n > 0} \in Q$. Thus $X \in Q_{\mathrm{loc}}$.

## Lean

Formalized as [`ProbabilityTheory.Locally.mono`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.Locally.mono).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 117](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L117)
