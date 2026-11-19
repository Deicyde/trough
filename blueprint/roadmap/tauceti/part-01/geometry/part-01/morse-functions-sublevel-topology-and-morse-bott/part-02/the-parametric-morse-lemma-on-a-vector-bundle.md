---
declaration: theorem
origin: cited
lean: TauCeti.exists_parametric_morse_partialDiffeomorph, TauCeti.exists_partialDiffeomorph_parametricMorseCoord
statement: formalized
proof: formalized
---

# The parametric Morse lemma on a vector bundle

Let `E → B` be a `C^{n+2}` vector bundle
with finite-dimensional normed fibres over a finite-dimensional, boundaryless, Hausdorff and
second-countable manifold, `1 ≤ n ≤ ∞`, and let `g` be `C^{n+2}` on an open neighbourhood `W` of
the zero section. Suppose that every zero vector `0_b` is a critical point
of the fibre restriction `v ↦ g ⟨b, v⟩` with invertible Hessian `H_b`. Then there is a single
`C^n` partial diffeomorphism `Φ` of the total space, with source in `W` containing the whole zero
section, of the form `Φ x = ⟨x.proj, ψ x⟩`, so preserving the fibres in both directions and fixing
the zero section, in which `g` is in fibrewise normal form:
`g x = g (0_b) + ½ H_b (ψ x) (ψ x)` for `x` over `b` in the source.

```lean
TauCeti.exists_parametric_morse_partialDiffeomorph.{u_1, u_2, u_3, u_4, u_5} {EB : Type u_1}
  [NormedAddCommGroup EB] [NormedSpace ℝ EB] {HB : Type u_2} [TopologicalSpace HB]
  {IB : ModelWithCorners ℝ EB HB} {B : Type u_3} [TopologicalSpace B] [ChartedSpace HB B]
  {F : Type u_4} [NormedAddCommGroup F] [NormedSpace ℝ F] {E : B → Type u_5}
  [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → NormedAddCommGroup (E b)] [FiberBundle F E]
  {g : Bundle.TotalSpace F E → ℝ} {W : Set (Bundle.TotalSpace F E)} [FiniteDimensional ℝ EB]
  [T2Space B] [SecondCountableTopology B] [IB.Boundaryless] [(b : B) → NormedSpace ℝ (E b)]
  [VectorBundle ℝ F E] [FiniteDimensional ℝ F] {n : ℕ∞} [IsManifold IB (↑n + 2) B]
  [ContMDiffVectorBundle (↑n + 2) F E IB] (hW : IsOpen W)
  (hzero : ∀ (b : B), Bundle.zeroSection F E b ∈ W)
  (hg : ContMDiffOn (IB.prod (modelWithCornersSelf ℝ F)) (modelWithCornersSelf ℝ ℝ) (↑n + 2) g W)
  (hcrit : ∀ (b : B), fderiv ℝ (fun v => g ⟨b, v⟩) 0 = 0)
  (hH : ∀ (b : B), (fderiv ℝ (fderiv ℝ fun v => g ⟨b, v⟩) 0).IsInvertible) (hn : n ≠ 0) :
  ∃ ψ Φ,
    (∀ (b : B), Bundle.zeroSection F E b ∈ Φ.source) ∧
      Φ.source ⊆ W ∧
        (∀ (x : Bundle.TotalSpace F E), ↑Φ.toPartialEquiv x = ⟨x.proj, ψ x⟩) ∧
          (∀ x ∈ Φ.target, (↑Φ.symm.toPartialEquiv x).proj = x.proj) ∧
            (∀ (b : B), ψ (Bundle.zeroSection F E b) = 0) ∧
              ∀ x ∈ Φ.source,
                g x =
                  g (Bundle.zeroSection F E x.proj) +
                    2⁻¹ * ((fderiv ℝ (fderiv ℝ fun v => g ⟨x.proj, v⟩) 0) (ψ x)) (ψ x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The local parametric Morse lemma](../../../../analysis/part-03/calculus/part-01/the-local-parametric-morse-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_parametric_morse_partialDiffeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Bott/VectorBundle.html#TauCeti.exists_parametric_morse_partialDiffeomorph).

## Other forms

**The parametric Morse lemma along the zero section over a manifold.** Formalized in Tau Ceti as [`TauCeti.exists_partialDiffeomorph_parametricMorseCoord`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/ZeroSectionChart.html#TauCeti.exists_partialDiffeomorph_parametricMorseCoord).

```lean
TauCeti.exists_partialDiffeomorph_parametricMorseCoord.{u_1, u_2, u_3, u_4} {EB : Type u_1}
  [NormedAddCommGroup EB] [NormedSpace ℝ EB] [FiniteDimensional ℝ EB] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ EB H} {S : Type u_3} [TopologicalSpace S]
  [ChartedSpace H S] {E : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  {F : S × E → ℝ} {W : Set (S × E)} {U : Set S} {n : ℕ∞} [IsManifold I (↑n + 2) S]
  [BoundarylessManifold I S] (hW : IsOpen W)
  (hF : ContMDiffOn (I.prod (modelWithCornersSelf ℝ E)) (modelWithCornersSelf ℝ ℝ) (↑n + 2) F W)
  (hU : IsOpen U) (hUW : ∀ b ∈ U, (b, 0) ∈ W) (hcrit : ∀ b ∈ U, fderiv ℝ (fun v => F (b, v)) 0 = 0)
  (hH : ∀ b ∈ U, (fderiv ℝ (fderiv ℝ fun v => F (b, v)) 0).IsInvertible) (hn : n ≠ 0) :
  ∃ ψ,
    ψ.source ⊆ W ∧
      (∀ b ∈ U, (b, 0) ∈ ψ.source) ∧
        (∀ z ∈ ψ.source, ∀ t ∈ Set.Icc 0 1, (z.1, t • z.2) ∈ ψ.source) ∧
          (∀ z ∈ ψ.source, ↑ψ.toPartialEquiv z = (z.1, TauCeti.parametricMorseCoord F z)) ∧
            (∀ z ∈ ψ.target, (↑ψ.symm.toPartialEquiv z).1 = z.1) ∧
              ∀ z ∈ ψ.source,
                F z =
                  F (z.1, 0) +
                    2⁻¹ *
                      ((fderiv ℝ (fderiv ℝ fun v => F (z.1, v)) 0) (↑ψ.toPartialEquiv z).2)
                        (↑ψ.toPartialEquiv z).2
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_parametric_morse_partialDiffeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Bott/VectorBundle.html#TauCeti.exists_parametric_morse_partialDiffeomorph)
- [Source of `TauCeti.exists_parametric_morse_partialDiffeomorph` in TauCeti/Geometry/Manifold/Morse/Bott/VectorBundle.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Morse/Bott/VectorBundle.lean#L380)
