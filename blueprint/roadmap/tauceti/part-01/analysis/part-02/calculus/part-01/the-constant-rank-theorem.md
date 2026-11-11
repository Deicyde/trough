---
declaration: theorem
origin: cited
lean: ContDiffOn.exists_openPartialHomeomorph_comp_eq_fderiv_comp
statement: formalized
proof: formalized
---

# The constant rank theorem

Let `f` be `C^n`, `1 ≤ n`, on an open subset `s` of a
finite-dimensional space, with values in a Banach space, and assume that the rank of `Df` on `s`
never exceeds its rank at `a ∈ s` (for instance, that it is constant on `s`). Then there are
charts `φ` of `E` near `a` and `ψ` of `F` near `f a`, `C^n` with `C^n` inverses, sending `a` and
`f a` to `0` with derivative the identity there, in which `f` is its derivative `L = Df(a)`:
`ψ (f x) = L (φ x)` for every `x` in the source of `φ`, a neighbourhood of `a` inside `s`.

```lean
ContDiffOn.exists_openPartialHomeomorph_comp_eq_fderiv_comp.{u_1, u_2, u_3} {𝕂 : Type u_1}
  [RCLike 𝕂] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕂 E] {F : Type u_3}
  [NormedAddCommGroup F] [NormedSpace 𝕂 F] [FiniteDimensional 𝕂 E] [CompleteSpace F]
  {n : WithTop ℕ∞} {f : E → F} {s : Set E} {a : E} (hf : ContDiffOn 𝕂 n f s) (hs : IsOpen s)
  (ha : a ∈ s) (hn : 1 ≤ n)
  (hrank :
    ∀ x ∈ s,
      Module.finrank 𝕂 ↥(↑(fderiv 𝕂 f x)).range ≤ Module.finrank 𝕂 ↥(↑(fderiv 𝕂 f a)).range) :
  ∃ φ ψ,
    a ∈ φ.source ∧
      φ.source ⊆ s ∧
        ↑φ a = 0 ∧
          HasFDerivAt (↑φ) (ContinuousLinearMap.id 𝕂 E) a ∧
            ContDiffOn 𝕂 n (↑φ) φ.source ∧
              ContDiffOn 𝕂 n (↑φ.symm) φ.target ∧
                ↑ψ (f a) = 0 ∧
                  HasFDerivAt (↑ψ) (ContinuousLinearMap.id 𝕂 F) (f a) ∧
                    ContDiffOn 𝕂 n (↑ψ) ψ.source ∧
                      ContDiffOn 𝕂 n (↑ψ.symm) ψ.target ∧
                        Set.MapsTo f φ.source ψ.source ∧
                          ∀ x ∈ φ.source, ↑ψ (f x) = (fderiv 𝕂 f a) (↑φ x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem, with a `C^n` inverse on the whole target](the-inverse-function-theorem-with-a-c-n-inverse.md)

## Lean

Formalized in Tau Ceti as [`ContDiffOn.exists_openPartialHomeomorph_comp_eq_fderiv_comp`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/ConstantRank.html#ContDiffOn.exists_openPartialHomeomorph_comp_eq_fderiv_comp).

## Sources

- [Tau Ceti documentation: `ContDiffOn.exists_openPartialHomeomorph_comp_eq_fderiv_comp`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/ConstantRank.html#ContDiffOn.exists_openPartialHomeomorph_comp_eq_fderiv_comp)
- [Source of `ContDiffOn.exists_openPartialHomeomorph_comp_eq_fderiv_comp` in TauCeti/Analysis/Calculus/ConstantRank.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/ConstantRank.lean#L108)
