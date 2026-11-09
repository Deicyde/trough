---
declaration: theorem
origin: cited
lean: Arxiv.«2607.03582».volume_lpSum_le, Arxiv.«2607.03582».volume_lpSum_eq_of_isParallelogramAtOrigin, Arxiv.«2607.03582».isParallelogramAtOrigin_of_volume_lpSum_eq
statement: formalized
---

# Planar $L_p$-Rogers-Shephard, the equality case

> *Reference:* [arxiv/2607.03582](https://arxiv.org/abs/2607.03582)
> **$L_p$-Rogers-Shephard type inequalities for $L_p$-zonoids and symmetric bodies**
> by *Matthieu Fradelizi, Auttawich Manui, Mark Meyer, Cheikh Saliou Ndiaye*
>
> *Formal proof of Conjecture 5:* Kenta Kitamura,
> [Lean proofs for the symmetric L_p Rogers–Shephard conjectures](https://github.com/KitaKen1/lp-rogers-shephard-conjectures-lean/tree/c646c668c0568b8533bf5534abcf02aab4d2df72).
>
> Corollary 29 bounds $|K \oplus_p -K|$ against $|K|$ for planar convex bodies with a centre of
> symmetry containing the origin, and notes that parallelograms with a vertex at the origin
> attain it. Conjecture 5 asks whether they are the only bodies that do.

*Quoted from [FormalConjectures/Arxiv/2607.03582/LpRogersShephard.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2607.03582/LpRogersShephard.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 solved. It also has 1 API statement, counted here but not shown.

## `Arxiv.«2607.03582».volume_lpSum_le`

Solved: stated here without proof.

> **Corollary 29 (Fradelizi-Manui-Meyer-Ndiaye, 2026).** For a planar convex body $K$ with a
> centre of symmetry containing the origin and $p > 1$,
> $$|K \oplus_p -K| \leq \left(\frac{2\Gamma(1+1/q)^2}{\Gamma(1+2/q)} + 2\right)|K|,$$
> where $q$ is the Hölder conjugate of $p$.

```lean
theorem volume_lpSum_le (K : Set ℝ²) (hK : Convex ℝ K) (hKc : IsCompact K)
    (hKi : (interior K).Nonempty) (hsym : HasCentreOfSymmetry K) (h0 : (0 : ℝ²) ∈ K)
    (p q : ℝ) (hp : 1 < p) (hq : 1 / p + 1 / q = 1) :
    volume (lpSum p K (-K)) ≤ ENNReal.ofReal (rsConstant q) * volume K
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Arxiv/2607.03582/LpRogersShephard.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2607.03582/LpRogersShephard.lean#L75).

## `Arxiv.«2607.03582».volume_lpSum_eq_of_isParallelogramAtOrigin`

Solved: stated here without proof.

> Parallelograms with a vertex at the origin attain the bound, which is the sharpness half of
> Corollary 29.

```lean
theorem volume_lpSum_eq_of_isParallelogramAtOrigin (K : Set ℝ²)
    (hpar : IsParallelogramAtOrigin K) (p q : ℝ) (hp : 1 < p) (hq : 1 / p + 1 / q = 1) :
    volume (lpSum p K (-K)) = ENNReal.ofReal (rsConstant q) * volume K
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Arxiv/2607.03582/LpRogersShephard.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2607.03582/LpRogersShephard.lean#L86).

## `Arxiv.«2607.03582».isParallelogramAtOrigin_of_volume_lpSum_eq`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/lp-rogers-shephard-conjectures-lean/blob/c646c668c0568b8533bf5534abcf02aab4d2df72/lean/LpRogersShephardFC.lean#L108-L128](https://github.com/KitaKen1/lp-rogers-shephard-conjectures-lean/blob/c646c668c0568b8533bf5534abcf02aab4d2df72/lean/LpRogersShephardFC.lean#L108-L128).

> **Conjecture 5 (Fradelizi-Manui-Meyer-Ndiaye, 2026).** Among planar convex bodies with a
> centre of symmetry containing the origin, for $p > 1$, equality in Corollary 29 holds only for
> parallelograms with a vertex at the origin.

```lean
theorem isParallelogramAtOrigin_of_volume_lpSum_eq :
    ∀ (K : Set ℝ²), Convex ℝ K → IsCompact K → (interior K).Nonempty →
      HasCentreOfSymmetry K → (0 : ℝ²) ∈ K → ∀ p q : ℝ, 1 < p → 1 / p + 1 / q = 1 →
        volume (lpSum p K (-K)) = ENNReal.ofReal (rsConstant q) * volume K →
          IsParallelogramAtOrigin K
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Arxiv/2607.03582/LpRogersShephard.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2607.03582/LpRogersShephard.lean#L100).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2607.03582/LpRogersShephard.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2607.03582/LpRogersShephard.lean)
- [arxiv/2607.03582](https://arxiv.org/abs/2607.03582)
