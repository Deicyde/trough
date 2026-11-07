---
declaration: theorem
origin: cited
lean: TauCeti.CStarAction.isKMSState_iff_of_dense
statement: formalized
proof: formalized
---

# Dense analytic KMS criterion

A state is β-KMS if and only if the analytic KMS
identity holds for pairs in a norm-dense invariant set of entire analytic elements.
In particular, the set can be a norm-dense invariant star subalgebra.

```lean
TauCeti.CStarAction.isKMSState_iff_of_dense.{u_1} {A : Type u_1} [NonUnitalCStarAlgebra A]
  {α : TauCeti.CStarAction (Multiplicative ℝ) A} {β : ℝ} [PartialOrder A] [StarOrderedRing A]
  {ω : A →P[ℂ] ℂ} {s : Set A} (hs : Dense s) (hinv : IsInvariant (fun t a => (α t) a) s)
  (hentire : ∀ b ∈ s, α.IsEntireAnalytic b) :
  α.IsKMSState β ω ↔
    ‖ω.toContinuousLinearMap‖ = 1 ∧
      ∀ a ∈ s, ∀ b ∈ s, ω (a * α.entireExtension b (↑β * Complex.I)) = ω (b * a)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Schwarz reflection principle (real axis)](../../part-02/conformal-mapping-and-the-geometric-theory-of-ho/schwarz-reflection-principle-real-axis.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.isKMSState_iff_of_dense`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/KMS/Dense.html#TauCeti.CStarAction.isKMSState_iff_of_dense).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.isKMSState_iff_of_dense`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/KMS/Dense.html#TauCeti.CStarAction.isKMSState_iff_of_dense)
- [Source of `TauCeti.CStarAction.isKMSState_iff_of_dense` in TauCeti/Analysis/CStarAlgebra/Action/KMS/Dense.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/CStarAlgebra/Action/KMS/Dense.lean#L106)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
