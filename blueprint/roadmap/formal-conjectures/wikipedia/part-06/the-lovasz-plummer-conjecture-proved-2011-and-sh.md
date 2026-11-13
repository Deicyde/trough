---
declaration: theorem
origin: cited
lean: LovaszPlummerConjecture.lovasz_plummer_conjecture, LovaszPlummerConjecture.lovasz_plummer_conjecture.variants.explicit, LovaszPlummerConjecture.sheehan_conjecture, LovaszPlummerConjecture.sheehan_conjecture.variants.thomassen
statement: formalized
---

# The Lovász–Plummer conjecture (proved 2011) and Sheehan's conjecture

> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Petersen%27s_theorem#Related_conjectures)
> * [LP86] Lovász, L. and Plummer, M. D. (1986). *Matching Theory.* North-Holland.
> * [EKKKN11] Esperet, L., Kardoš, F., King, A. D., Král', D. and Norine, S. (2011).
>   "Exponentially many perfect matchings in cubic graphs." *Adv. Math.* 227, pp. 1646--1664.
>   [arXiv:1012.2878](https://arxiv.org/abs/1012.2878)
> * [Sh77] Sheehan, J. (1977). "The multiplicity of Hamiltonian circuits in a graph." In *Recent
>   Advances in Graph Theory*, Academia, Prague, pp. 477--480.
> * [Th98] Thomassen, C. (1998). "Independent dominating sets and a second Hamiltonian cycle in
>   regular graphs." *J. Combin. Theory Ser. B* 72, pp. 104--109.

*Quoted from [FormalConjectures/Wikipedia/LovaszPlummerConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LovaszPlummerConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 1 open and 3 solved.

## `LovaszPlummerConjecture.lovasz_plummer_conjecture`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/da6d56610c43a6eadd15945a3b80a62f223293f8/Proofs/T_LovaszPlummerConjecture_lovasz_plummer_conjecture.lean#L16602](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/da6d56610c43a6eadd15945a3b80a62f223293f8/Proofs/T_LovaszPlummerConjecture_lovasz_plummer_conjecture.lean#L16602).

> **The Lovász–Plummer conjecture (1970s), proved by Esperet, Kardoš, King, Král' and Norine
> (2011).**
>
> Every bridgeless cubic graph on $n$ vertices has exponentially many perfect matchings: there is
> a constant $c > 0$ such that the number of perfect matchings is at least $2^{cn}$.
> [EKKKN11] prove this with $2^{n/3656}$.

```lean
theorem lovasz_plummer_conjecture :
    ∃ c : ℝ, 0 < c ∧ ∀ {V : Type} [Fintype V] [DecidableEq V]
      (G : SimpleGraph V) [DecidableRel G.Adj],
      (∀ v, G.degree v = 3) → G.IsBridgeless →
      (2 : ℝ) ^ (c * Fintype.card V) ≤ perfectMatchingCount G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/LovaszPlummerConjecture.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LovaszPlummerConjecture.lean#L57).

## `LovaszPlummerConjecture.lovasz_plummer_conjecture.variants.explicit`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/e1059f02264088e9fc4e2866855b8cf68d9cbeda/Proofs/T_LovaszPlummerConjecture_lovasz_plummer_conjecture_variants_explicit.lean#L34280](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/e1059f02264088e9fc4e2866855b8cf68d9cbeda/Proofs/T_LovaszPlummerConjecture_lovasz_plummer_conjecture_variants_explicit.lean#L34280).

> **The explicit bound of Esperet–Kardoš–King–Král'–Norine (2011).**
>
> Every bridgeless cubic graph on $n$ vertices has at least $2^{n/3656}$ perfect matchings.
>
> *Reference:* [EKKKN11].

```lean
theorem lovasz_plummer_conjecture.variants.explicit
    {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj]
    (hcubic : ∀ v, G.degree v = 3) (hbridgeless : G.IsBridgeless) :
    (2 : ℝ) ^ ((Fintype.card V : ℝ) / 3656) ≤ perfectMatchingCount G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/LovaszPlummerConjecture.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LovaszPlummerConjecture.lean#L73).

## `LovaszPlummerConjecture.sheehan_conjecture`

Open: stated without proof.

> **Sheehan's conjecture (1977).**
>
> Every $4$-regular graph with a Hamiltonian cycle has a second Hamiltonian cycle (one with a
> different edge set). Sheehan's conjecture would settle the last open case of the question,
> raised by Smith's theorem for cubic graphs, of which regular Hamiltonian graphs have a second
> Hamiltonian cycle: Thomassen [Th98] proved it for all $r$-regular graphs with $r \ge 300$.

```lean
theorem sheehan_conjecture :
    ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
      (∀ v, G.degree v = 4) →
      ∀ (v : V) (c : G.Walk v v), IsHamiltonianCycle G c →
        ∃ (w : V) (c' : G.Walk w w), IsHamiltonianCycle G c' ∧
          c'.edges.toFinset ≠ c.edges.toFinset
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/LovaszPlummerConjecture.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LovaszPlummerConjecture.lean#L92).

## `LovaszPlummerConjecture.sheehan_conjecture.variants.thomassen`

Solved: stated here without proof.

> **Thomassen (1998): regular graphs of large degree.**
>
> Every $r$-regular Hamiltonian graph with $r \ge 300$ has a second Hamiltonian cycle.
>
> *Reference:* [Th98].

```lean
theorem sheehan_conjecture.variants.thomassen
    {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj]
    (r : ℕ) (hr : 300 ≤ r) (hreg : ∀ v, G.degree v = r)
    (v : V) (c : G.Walk v v) (hc : IsHamiltonianCycle G c) :
    ∃ (w : V) (c' : G.Walk w w), IsHamiltonianCycle G c' ∧
      c'.edges.toFinset ≠ c.edges.toFinset
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/LovaszPlummerConjecture.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LovaszPlummerConjecture.lean#L108).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/LovaszPlummerConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LovaszPlummerConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Petersen%27s_theorem#Related_conjectures)
