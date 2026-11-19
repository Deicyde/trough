---
declaration: theorem
origin: cited
lean: TauCeti.exists_openPartialHomeomorph_tendstoContDiffAt_symm, TauCeti.ContDiffOn.exists_openPartialHomeomorph
statement: formalized
proof: formalized
---

# The inverse function theorem for a converging family

Let `Φ i → Φ₀` in `C^n` at every
point of an open set `s`, with `1 ≤ n`, the maps `Φ i` eventually `C^n` on `s`, and `D Φ₀`
invertible at `x₀ ∈ s`. Then `Φ₀` and, eventually along `l`, all the `Φ i` restrict to partial
homeomorphisms with one common source inside `s`, whose targets contain a common open
neighbourhood `T` of `Φ₀ (x₀)` and whose inverses are `C^n` on their targets. On `T` the inverses
converge to the inverse of `Φ₀` in `C^n`.

```lean
TauCeti.exists_openPartialHomeomorph_tendstoContDiffAt_symm.{u_5, u_6, u_7, u_8} {𝕜 : Type u_5}
  [RCLike 𝕜] {E : Type u_6} [NormedAddCommGroup E] [NormedSpace 𝕜 E] [CompleteSpace E]
  {F : Type u_7} [NormedAddCommGroup F] [NormedSpace 𝕜 F] {ι : Type u_8} {l : Filter ι} {n : ℕ}
  {Φ : ι → E → F} {Φ₀ : E → F} {s : Set E} {x₀ : E} (hs : IsOpen s) (hx₀ : x₀ ∈ s) (hn : 1 ≤ n)
  (hΦ : ∀ᶠ (i : ι) in l, ContDiffOn 𝕜 (↑n) (Φ i) s) (hΦ₀ : ContDiffOn 𝕜 (↑n) Φ₀ s)
  (hconv : ∀ x ∈ s, TauCeti.TendstoContDiffAt 𝕜 n Φ Φ₀ l x) (hinv : (fderiv 𝕜 Φ₀ x₀).IsInvertible) :
  ∃ e₀ e T,
    IsOpen T ∧
      Φ₀ x₀ ∈ T ∧
        ↑e₀ = Φ₀ ∧
          x₀ ∈ e₀.source ∧
            e₀.source ⊆ s ∧
              T ⊆ e₀.target ∧
                ContDiffOn 𝕜 (↑n) (↑e₀.symm) e₀.target ∧
                  (∀ᶠ (i : ι) in l,
                      ↑(e i) = Φ i ∧
                        (e i).source = e₀.source ∧
                          T ⊆ (e i).target ∧ ContDiffOn 𝕜 (↑n) (↑(e i).symm) (e i).target) ∧
                    ∀ y ∈ T, TauCeti.TendstoContDiffAt 𝕜 n (fun i => ↑(e i).symm) (↑e₀.symm) l y
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_openPartialHomeomorph_tendstoContDiffAt_symm`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/InverseFunctionTheorem/Family.html#TauCeti.exists_openPartialHomeomorph_tendstoContDiffAt_symm).

## Other forms

**The inverse function theorem, with a `C^n` inverse on the whole target.** Formalized in Tau Ceti as [`TauCeti.ContDiffOn.exists_openPartialHomeomorph`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/InverseFunctionTheorem.html#TauCeti.ContDiffOn.exists_openPartialHomeomorph).

```lean
TauCeti.ContDiffOn.exists_openPartialHomeomorph.{u_1, u_2, u_3} {𝕂 : Type u_1} [RCLike 𝕂]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕂 E] [CompleteSpace E] {F : Type u_3}
  [NormedAddCommGroup F] [NormedSpace 𝕂 F] {n : WithTop ℕ∞} {g : E → F} {s : Set E} {a : E}
  (hg : ContDiffOn 𝕂 n g s) (hs : IsOpen s) (ha : a ∈ s) (hn : 1 ≤ n) {e : E ≃L[𝕂] F}
  (he : ↑e = fderiv 𝕂 g a) :
  ∃ Θ, ↑Θ = g ∧ a ∈ Θ.source ∧ Θ.source ⊆ s ∧ ContDiffOn 𝕂 n (↑Θ.symm) Θ.target
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_openPartialHomeomorph_tendstoContDiffAt_symm`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/InverseFunctionTheorem/Family.html#TauCeti.exists_openPartialHomeomorph_tendstoContDiffAt_symm)
- [Source of `TauCeti.exists_openPartialHomeomorph_tendstoContDiffAt_symm` in TauCeti/Analysis/Calculus/InverseFunctionTheorem/Family.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/InverseFunctionTheorem/Family.lean#L216)
