---
declaration: section
origin: cited
lean: OAI.HenonLaneEmden.main_nonexistence
statement: formalized
proof: formalized
---

# 370. The Lane–Emden and Hénon–Lane–Emden conjectures

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the subcritical Lane–Emden conjecture and its weighted Hénon extension. For *n* ≥ 2, $p,q\gt 0$ and real *A*, *B*, the system $-\Delta u=|x|^A v^p$, $-\Delta v=|x|^B u^q$ has no positive entire solution when $(n+A)/(p+1)+(n+B)/(q+1)\gt n-2$, with solutions continuous at the origin and classical elsewhere. No symmetry or growth assumption is needed. Known radial existence gives the exact existence criterion for *n* ≥ 3 and $A,B\gt -2$.

## The Subcritical Hénon–Lane–Emden Conjecture

We prove the subcritical Hénon–Lane–Emden conjecture: for every dimension *n* ≥ 2, positive powers *p*, *q*, and real weights *A*, *B*, the system has no strictly positive entire solution when $(n+A)/(p+1)+(n+B)/(q+1)\gt n-2$. Solutions need only be continuous at the origin and classical elsewhere, without a condition at infinity. For *n* ≥ 3 and $A,B\gt -2$, combining this result with the radial existence theorem of Bidaut-Véron and Giacomini proves Phan's Conjecture C in full: a positive radial entire solution exists whenever the strict inequality fails.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result proves nonexistence of positive entire solutions to the subcritical Hénon–Lane–Emden system. For $n\ge2$, $p,q>0$, and real $A,B$ with $(n+A)/(p+1)+(n+B)/(q+1)>n-2$, there are no positive functions, continuous everywhere and $C^2$ off the origin, satisfying $-\Delta u=|x|^A v^p$ and $-\Delta v=|x|^B u^q$ away from the origin. It includes the globally $C^2$ unweighted case for $n\ge3$. The critical equality case is not included.

## Lean: Subcritical Hénon–Lane–Emden nonexistence

```lean
theorem main_nonexistence (n : ℕ) (hn : 2 ≤ n) (p q A B : ℝ)
    (hp : 0 < p) (hq : 0 < q) (hsub : Subcritical n p q A B) :
    ¬ ∃ u v : Space n → ℝ, IsSolution n p q A B u v
```

Stated in [HenonEmden.lean, line 24](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HenonEmden.lean#L24). Proved in [lean/OAI/Analysis/HenonEmden/Main.lean, line 9](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/HenonEmden/Main.lean#L9). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/370.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/370.md)
