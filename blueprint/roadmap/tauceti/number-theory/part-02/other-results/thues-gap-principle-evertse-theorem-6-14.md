---
declaration: theorem
origin: cited
lean: TauCeti.thue_gap_principle
statement: formalized
proof: formalized
---

# Thue's gap principle (Evertse, Theorem 6.14)

Let `α` be a complex algebraic number of
degree `d ≥ 2` and let `κ > d / 2 + 1`. There are constants `C ≥ 1` and `λ ≥ 1` such that for
all rationals `ξ₁` and `ξ` with `|ξ₁ - α| ≤ H(ξ₁) ^ (-κ)`, `H(ξ₁) ≥ C` and
`|ξ - α| ≤ H(ξ) ^ (-κ)`, the heights satisfy `H(ξ) ≤ H(ξ₁) ^ λ`. The degree hypothesis
already forces `α` to be algebraic.

```lean
TauCeti.thue_gap_principle {α : ℂ} (hd : 2 ≤ (minpoly ℚ α).natDegree) {κ : ℝ}
  (hκ : ↑(minpoly ℚ α).natDegree / 2 + 1 < κ) :
  ∃ C lam,
    1 ≤ C ∧
      1 ≤ lam ∧
        ∀ (ξ₁ ξ : ℚ),
          ‖↑ξ₁ - α‖ ≤ Height.mulHeight₁ ξ₁ ^ (-κ) →
            C ≤ Height.mulHeight₁ ξ₁ →
              ‖↑ξ - α‖ ≤ Height.mulHeight₁ ξ ^ (-κ) →
                Height.mulHeight₁ ξ ≤ Height.mulHeight₁ ξ₁ ^ lam
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Siegel's lemma for a rational subspace, in the sup norm](../../part-01/heights-units-and-s-units-of-number-fields/part-02/siegels-lemma-for-a-rational-subspace-in-the-sup.md)
- [The Wronskian criterion](../../../geometry/part-01/real-algebraic-geometry-sign-determination-and-c/the-wronskian-criterion.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.thue_gap_principle`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Thue/GapPrinciple.html#TauCeti.thue_gap_principle).

## Sources

- [Tau Ceti documentation: `TauCeti.thue_gap_principle`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Thue/GapPrinciple.html#TauCeti.thue_gap_principle)
- [Source of `TauCeti.thue_gap_principle` in TauCeti/NumberTheory/DiophantineApproximation/Thue/GapPrinciple.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/DiophantineApproximation/Thue/GapPrinciple.lean#L86)
