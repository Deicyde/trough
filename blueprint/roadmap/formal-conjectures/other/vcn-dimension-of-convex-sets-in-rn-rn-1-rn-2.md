---
declaration: lemma
origin: cited
lean: VCDimConvex.hasAddVCDimAtMost_three_of_convex_r2, VCDimConvex.exists_infinite_convex_r3_shatters, VCDimConvex.exists_convex_rn_add_two_vc_n_forall_not_hasAddVCNDimAtMost, VCDimConvex.hasAddVCNDimAtMost_two_one_of_convex_r3, VCDimConvex.hasAddVCNDimAtMost_two_two_of_convex_r3, VCDimConvex.exists_hasAddVCNDimAtMost_n_of_convex_rn_add_one, VCDimConvex.exists_exponential_bound_hasAddVCNDimAtMost_n_of_convex_rn_add_one, VCDimConvex.hasAddVCNDimAtMost_n_two_of_convex_rn_add_one
statement: formalized
---

# VCₙ dimension of convex sets in ℝⁿ, ℝⁿ⁺¹, ℝⁿ⁺²

> In the literature it is known that every convex set in ℝ² has VC dimension at most 3,
> and there exists a convex set in ℝ³ with infinite VC dimension (even more strongly,
> which shatters an infinite set).
>
> This file states that every convex set in ℝⁿ has finite VCₙ dimension, constructs a convex set in
> ℝⁿ⁺² with infinite VCₙ dimension (even more strongly, which n-shatters an infinite set),
> and conjectures that every convex set in ℝⁿ⁺¹ has finite VCₙ dimension.

*Quoted from [FormalConjectures/Other/VCDimConvex.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Other/VCDimConvex.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 8 research or textbook statements: 3 open and 5 solved.

## `VCDimConvex.hasAddVCDimAtMost_three_of_convex_r2`

Solved: stated here without proof.

> Every convex set in $\mathbb R^2$ has VC dimension at most 3.

```lean
lemma hasAddVCDimAtMost_three_of_convex_r2 {C : Set ℝ²} (hC : Convex ℝ C) : HasAddVCDimAtMost C 3
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Other/VCDimConvex.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Other/VCDimConvex.lean#L42).

## `VCDimConvex.exists_infinite_convex_r3_shatters`

Solved: stated here without proof.

> There exists a set in $\mathbb R^3$ shattering an infinite set.

```lean
lemma exists_infinite_convex_r3_shatters :
    ∃ A C : Set ℝ³, A.Infinite ∧ Convex ℝ C ∧ Shatters {t +ᵥ C | t : ℝ³} A
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Other/VCDimConvex.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Other/VCDimConvex.lean#L47).

## `VCDimConvex.exists_convex_rn_add_two_vc_n_forall_not_hasAddVCNDimAtMost`

Solved: stated here without proof.

> There exists a set of infinite $\mathrm{VC}_n$ dimension in $\mathbb R^{n + 2}$.

```lean
lemma exists_convex_rn_add_two_vc_n_forall_not_hasAddVCNDimAtMost (n : ℕ) :
    ∃ C : Set (Fin (n + 2) → ℝ), Convex ℝ C ∧ ∀ d, ¬ HasAddVCNDimAtMost C n d
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Other/VCDimConvex.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Other/VCDimConvex.lean#L54).

## `VCDimConvex.hasAddVCNDimAtMost_two_one_of_convex_r3`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/vcdim-convex-counterexample/blob/ad7ffff1514843c886633f5408c6456dfb2e2a49/formal-conjectures-v4.27.0/VCDimConvexCounterexample.lean](https://github.com/KitaKen1/vcdim-convex-counterexample/blob/ad7ffff1514843c886633f5408c6456dfb2e2a49/formal-conjectures-v4.27.0/VCDimConvexCounterexample.lean).

> Not every convex set in $\mathbb R^3$ has
> $\mathrm{VC}_2$ dimension at most 1.

```lean
lemma hasAddVCNDimAtMost_two_one_of_convex_r3 :
    ¬ ∀ {C : Set ℝ³} (hC : Convex ℝ C),
      HasAddVCNDimAtMost C 2 1
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Other/VCDimConvex.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Other/VCDimConvex.lean#L65).

## `VCDimConvex.hasAddVCNDimAtMost_two_two_of_convex_r3`

Open: stated without proof.

> Every convex set in $\mathbb R^3$ has $\mathrm{VC}_2$ dimension at most 2.

```lean
lemma hasAddVCNDimAtMost_two_two_of_convex_r3 {C : Set ℝ³} (hC : Convex ℝ C) :
    HasAddVCNDimAtMost C 2 2
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Other/VCDimConvex.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Other/VCDimConvex.lean#L71).

## `VCDimConvex.exists_hasAddVCNDimAtMost_n_of_convex_rn_add_one`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/vcdim-convex-finite-bound/blob/9d7685c7c7c8c8e82f47d59da5495a8d5374db99/lean/VCDimConvexBoundFC.lean#L14-L17](https://github.com/KitaKen1/vcdim-convex-finite-bound/blob/9d7685c7c7c8c8e82f47d59da5495a8d5374db99/lean/VCDimConvexBoundFC.lean#L14-L17).

> For every $n \ge 1$ there exists some $d$ such that every convex set in $\mathbb R^{n + 1}$ has
> $\mathrm{VC}_n$ dimension at most $d$.
>
> This holds with the explicit bound $d = 2^{8(n + 2)^n} - 1$; see
> [Kitamura's Lean formalization](https://github.com/KitaKen1/vcdim-convex-finite-bound).

```lean
lemma exists_hasAddVCNDimAtMost_n_of_convex_rn_add_one (n : ℕ) (hn : 1 ≤ n) :
    ∃ d : ℕ, ∀ C : Set (Fin (n + 1) → ℝ), Convex ℝ C → HasAddVCNDimAtMost C n d
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Other/VCDimConvex.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Other/VCDimConvex.lean#L84).

## `VCDimConvex.exists_exponential_bound_hasAddVCNDimAtMost_n_of_convex_rn_add_one`

Open: stated without proof.

> For every $n \ge 1$ there exists some $d$ such that every convex set in $\mathbb R^{n + 1}$ has
> $\mathrm{VC}_n$ dimension at most $d$.
>
> The bound can be taken to be $d = c^n$ for some constant $c \ge 2$ independent of $n$.

```lean
lemma exists_exponential_bound_hasAddVCNDimAtMost_n_of_convex_rn_add_one :
    ∃ c : ℕ, 2 ≤ c ∧ ∀ (n : ℕ) (hn : 1 ≤ n),
      ∀ C : Set (Fin (n + 1) → ℝ), Convex ℝ C → HasAddVCNDimAtMost C n (c ^ n)
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Other/VCDimConvex.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Other/VCDimConvex.lean#L93).

## `VCDimConvex.hasAddVCNDimAtMost_n_two_of_convex_rn_add_one`

Open: stated without proof.

> Is it true that, for all $n$, every convex set in $\mathbb R^{n + 1}$ has
> $\mathrm{VC}_n$ dimension at most 3?

```lean
lemma hasAddVCNDimAtMost_n_two_of_convex_rn_add_one :
    ∀ ⦃n : ℕ⦄, n ≠ 0 → ∀ ⦃C : Set (EuclideanSpace ℝ (Fin (n + 1)))⦄,
      Convex ℝ C → HasAddVCNDimAtMost C n 3
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Other/VCDimConvex.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Other/VCDimConvex.lean#L100).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Other/VCDimConvex.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Other/VCDimConvex.lean)
