---
declaration: theorem
origin: cited
lean: TauCeti.NovikovModule.kernelProduct_kernelProduct_sub_kernelProduct_kernelProduct_mem_coboundaries
statement: formalized
proof: formalized
---

# Associativity on cocycles

Under the kernel homotopy of
`NovikovModule.kernelProduct_kernelProduct_sub_kernelProduct_kernelProduct_of_mem_gradeBy`, if the
homotopy kernel `k` shifts degree by `ε - 1`, then for cocycles `a`, `b`, `c` of degrees `i`, `j`,
`l` the difference `(a ⋆ b) ⋆' c - a ⋆''' (b ⋆'' c)` is a coboundary of degree `i + j + l + ε`.

```lean
TauCeti.NovikovModule.kernelProduct_kernelProduct_sub_kernelProduct_kernelProduct_mem_coboundaries.{u_1,
    u_2, u_3, u_4, u_5, u_6, u_7}
  {R : Type u_1} {S₁ : Type u_2} {S₂ : Type u_3} {S₃ : Type u_4} {S₀ : Type u_5} {S₁₂ : Type u_6}
  {S₂₃ : Type u_7} {F₁ : S₁ → ℝ} {F₂ : S₂ → ℝ} {F₃ : S₃ → ℝ} {F₀ : S₀ → ℝ} {F₁₂ : S₁₂ → ℝ}
  {F₂₃ : S₂₃ → ℝ} [CommRing R] {C₁ C₂ C₃ C₄ Ck C₀ : ℝ} {n : S₁ → S₂ → S₁₂ → R}
  {n' : S₁₂ → S₃ → S₀ → R} {m : S₂ → S₃ → S₂₃ → R} {m' : S₁ → S₂₃ → S₀ → R}
  {k : (S₁ × S₂) × S₃ → S₀ → R} {δ₀ : S₀ → S₀ → R}
  (hn : ∀ (p₁ : S₁) (p₂ : S₂) (t : S₁₂), n p₁ p₂ t ≠ 0 → F₁₂ t ≤ F₁ p₁ + F₂ p₂ + C₁)
  (hfin : ∀ (p₁ : S₁) (p₂ : S₂), n p₁ p₂ ∈ TauCeti.NovikovModule R F₁₂)
  (hn' : ∀ (t : S₁₂) (p₃ : S₃) (p₀ : S₀), n' t p₃ p₀ ≠ 0 → F₀ p₀ ≤ F₁₂ t + F₃ p₃ + C₂)
  (hfin' : ∀ (t : S₁₂) (p₃ : S₃), n' t p₃ ∈ TauCeti.NovikovModule R F₀)
  (hm : ∀ (p₂ : S₂) (p₃ : S₃) (u : S₂₃), m p₂ p₃ u ≠ 0 → F₂₃ u ≤ F₂ p₂ + F₃ p₃ + C₃)
  (hmfin : ∀ (p₂ : S₂) (p₃ : S₃), m p₂ p₃ ∈ TauCeti.NovikovModule R F₂₃)
  (hm' : ∀ (p₁ : S₁) (u : S₂₃) (p₀ : S₀), m' p₁ u p₀ ≠ 0 → F₀ p₀ ≤ F₁ p₁ + F₂₃ u + C₄)
  (hmfin' : ∀ (p₁ : S₁) (u : S₂₃), m' p₁ u ∈ TauCeti.NovikovModule R F₀)
  (hk : ∀ (q : (S₁ × S₂) × S₃) (p₀ : S₀), k q p₀ ≠ 0 → F₀ p₀ ≤ F₁ q.1.1 + F₂ q.1.2 + F₃ q.2 + Ck)
  (hkfin : ∀ (q : (S₁ × S₂) × S₃), k q ∈ TauCeti.NovikovModule R F₀)
  (hδ₀ : ∀ (p p₀ : S₀), δ₀ p p₀ ≠ 0 → F₀ p₀ ≤ F₀ p + C₀)
  (hδ₀fin : ∀ (p : S₀), δ₀ p ∈ TauCeti.NovikovModule R F₀) [DecidableEq S₁] [DecidableEq S₂]
  [DecidableEq S₃] {d₁ : S₁ → ℤ} {d₂ : S₂ → ℤ} {d₃ : S₃ → ℤ} {d₀ : S₀ → ℤ} {δ₁ : S₁ → S₁ → R}
  {δ₂ : S₂ → S₂ → R} {δ₃ : S₃ → S₃ → R} {E₁ E₂ E₃ : ℝ}
  (hδ₁ : ∀ (p q : S₁), δ₁ p q ≠ 0 → F₁ q ≤ F₁ p + E₁)
  (hδ₁fin : ∀ (p : S₁), δ₁ p ∈ TauCeti.NovikovModule R F₁)
  (hδ₂ : ∀ (p q : S₂), δ₂ p q ≠ 0 → F₂ q ≤ F₂ p + E₂)
  (hδ₂fin : ∀ (p : S₂), δ₂ p ∈ TauCeti.NovikovModule R F₂)
  (hδ₃ : ∀ (p q : S₃), δ₃ p q ≠ 0 → F₃ q ≤ F₃ p + E₃)
  (hδ₃fin : ∀ (p : S₃), δ₃ p ∈ TauCeti.NovikovModule R F₃) {ε : ℤ}
  (hkd :
    ∀ (q : (S₁ × S₂) × S₃) (p₀ : S₀), k q p₀ ≠ 0 → d₀ p₀ = d₁ q.1.1 + d₂ q.1.2 + d₃ q.2 + (ε - 1))
  (hassoc :
    ∀ (q : (S₁ × S₂) × S₃) (p₀ : S₀),
      ∑ᶠ (t : S₁₂), n q.1.1 q.1.2 t * n' t q.2 p₀ - ∑ᶠ (u : S₂₃), m q.1.2 q.2 u * m' q.1.1 u p₀ =
        TauCeti.NovikovModule.kernelComp k δ₀ q p₀ +
          TauCeti.NovikovModule.kernelComp
            (TauCeti.NovikovModule.tensorDifferential (fun q => d₁ q.1 + d₂ q.2)
              (TauCeti.NovikovModule.tensorDifferential d₁ δ₁ δ₂) δ₃)
            k q p₀)
  {i j l : ℤ} {a : ↥(TauCeti.NovikovModule R F₁)}
  (ha :
    a ∈
      (TauCeti.NovikovModule.kernelMap hδ₁ hδ₁fin).cocycles (TauCeti.NovikovModule.gradeBy R F₁ d₁)
        i)
  {b : ↥(TauCeti.NovikovModule R F₂)}
  (hb :
    b ∈
      (TauCeti.NovikovModule.kernelMap hδ₂ hδ₂fin).cocycles (TauCeti.NovikovModule.gradeBy R F₂ d₂)
        j)
  {c : ↥(TauCeti.NovikovModule R F₃)}
  (hc :
    c ∈
      (TauCeti.NovikovModule.kernelMap hδ₃ hδ₃fin).cocycles (TauCeti.NovikovModule.gradeBy R F₃ d₃)
        l) :
  ((TauCeti.NovikovModule.kernelProduct hn' hfin')
          (((TauCeti.NovikovModule.kernelProduct hn hfin) a) b))
        c -
      ((TauCeti.NovikovModule.kernelProduct hm' hmfin') a)
        (((TauCeti.NovikovModule.kernelProduct hm hmfin) b) c) ∈
    (TauCeti.NovikovModule.kernelMap hδ₀ hδ₀fin).coboundaries
      (TauCeti.NovikovModule.gradeBy R F₀ d₀) (i + j + l + ε)
```

## Depends on

- [TauCeti.NovikovModule.kernelProduct](tauceti-novikovmodule-kernelproduct.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NovikovModule.kernelProduct_kernelProduct_sub_kernelProduct_kernelProduct_mem_coboundaries`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovModule/Associativity.html#TauCeti.NovikovModule.kernelProduct_kernelProduct_sub_kernelProduct_kernelProduct_mem_coboundaries).

## Sources

- [Tau Ceti documentation: `TauCeti.NovikovModule.kernelProduct_kernelProduct_sub_kernelProduct_kernelProduct_mem_coboundaries`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovModule/Associativity.html#TauCeti.NovikovModule.kernelProduct_kernelProduct_sub_kernelProduct_kernelProduct_mem_coboundaries)
- [Source of `TauCeti.NovikovModule.kernelProduct_kernelProduct_sub_kernelProduct_kernelProduct_mem_coboundaries` in TauCeti/RingTheory/NovikovModule/Associativity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/NovikovModule/Associativity.lean#L305)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
