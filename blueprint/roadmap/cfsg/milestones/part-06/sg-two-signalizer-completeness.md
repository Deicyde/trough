---
declaration: theorem
origin: cited
lean: CFSG.Milestones.sg_two_signalizer_completeness
statement: formalized
proof: formalized
---

# SG_two_signalizer_completeness

The milestone module `CFSG.Milestones.SG_two_signalizer_completeness`, one of those CFSG/Milestones.lean imports.

It declares 1 result, quoted from [CFSG/Milestones/SG_two_signalizer_completeness.lean](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/SG_two_signalizer_completeness.lean) in [AxiomMath/CFSG](https://github.com/AxiomMath/CFSG) at commit [69cb972f](https://github.com/AxiomMath/CFSG/tree/69cb972f587a3ecc035e092253167ff2e303c962), Apache-2.0:

`CFSG.Milestones.sg_two_signalizer_completeness` (theorem, [line 46](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/SG_two_signalizer_completeness.lean#L46)). Proved here.

```lean
theorem _root_.CFSG.Milestones.sg_two_signalizer_completeness
    (G : Type) [Group G] [Finite G]
    (A : Type) [CommGroup A] [Finite A] (hexp : ∀ a : A, a ^ 2 = 1) (hcard : 8 ≤ Nat.card A)
    (α : A →* MulAut G) (θ : A → Subgroup G)
    (hinv : ∀ a : A, a ≠ 1 → ∀ b : A, (θ a).map (α b).toMonoidHom = θ a)
    (hsolv : ∀ a : A, a ≠ 1 → Group.IsSolvable (θ a))
    (hodd : ∀ a : A, a ≠ 1 → Odd (Nat.card (θ a)))
    (hcent : ∀ a : A, a ≠ 1 → ∀ g ∈ θ a, α a g = g)
    (hbal : ∀ a b : A, a ≠ 1 → b ≠ 1 → ∀ g ∈ θ a, α b g = g → g ∈ θ b) :
    let Θ : Subgroup G := ⨆ (a : A) (_ : a ≠ 1), θ a
    (∀ b : A, Θ.map (α b).toMonoidHom = Θ) ∧ Group.IsSolvable Θ ∧ Odd (Nat.card Θ) ∧
      ∀ a : A, a ≠ 1 → ∀ g : G, (g ∈ Θ ∧ α a g = g ↔ g ∈ θ a)
```

The files of 3 case theorems import it, directly or through other files: [`CFSG.Assembly.component_type`](../../case-division/case-hcomp-componentstatement.md), [`CFSG.Assembly.rank_three_even`](../../case-division/case-hr3-rankthreestatement.md), [`CFSG.Assembly.large_even`](../../case-division/case-hle-largeevenstatement.md).

## Depends on

Its Lean file imports no case or milestone file, directly or through other files.

## Sources

- [CFSG/Milestones/SG_two_signalizer_completeness.lean at 69cb972f](https://github.com/AxiomMath/CFSG/blob/69cb972f587a3ecc035e092253167ff2e303c962/CFSG/Milestones/SG_two_signalizer_completeness.lean)
