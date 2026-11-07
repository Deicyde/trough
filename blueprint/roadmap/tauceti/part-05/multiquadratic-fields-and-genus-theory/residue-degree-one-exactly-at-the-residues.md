---
declaration: theorem
origin: cited
lean: TauCeti.Multiquadratic.inertiaDeg_eq_one_iff_forall_legendreSym_eq_one
statement: formalized
proof: formalized
---

# Residue degree one exactly at the residues

Let `K` be generated over `ℚ` by square roots
`r i` of integers `d i`, and let `Q` be a prime of `𝓞 K` above an odd prime `p` dividing none of
the `d i`. Then `Q` has residue degree `1` iff every `d i` is a quadratic residue mod `p`.

```lean
TauCeti.Multiquadratic.inertiaDeg_eq_one_iff_forall_legendreSym_eq_one.{u_1, u_2} {K : Type u_1}
  [Field K] [NumberField K] {ι : Type u_2} {d : ι → ℤ} {r : ι → K} {p : ℕ} [Fact (Nat.Prime p)]
  [Finite ι] (hr : ∀ (i : ι), r i ^ 2 = (algebraMap ℤ K) (d i))
  (htop : IntermediateField.adjoin ℚ (Set.range r) = ⊤) (hodd : p ≠ 2) (hcop : ∀ (i : ι), ¬↑p ∣ d i)
  (Q : Ideal (NumberField.RingOfIntegers K)) [Q.IsPrime] [Q.LiesOver (Ideal.span {↑p})] :
  Q.inertiaDeg ℤ = 1 ↔ ∀ (i : ι), legendreSym p (d i) = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Multiquadratic.inertiaDeg_eq_one_iff_forall_legendreSym_eq_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/ResidueDegree.html#TauCeti.Multiquadratic.inertiaDeg_eq_one_iff_forall_legendreSym_eq_one).

## Sources

- [Tau Ceti documentation: `TauCeti.Multiquadratic.inertiaDeg_eq_one_iff_forall_legendreSym_eq_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/ResidueDegree.html#TauCeti.Multiquadratic.inertiaDeg_eq_one_iff_forall_legendreSym_eq_one)
- [Source of `TauCeti.Multiquadratic.inertiaDeg_eq_one_iff_forall_legendreSym_eq_one` in TauCeti/NumberTheory/Multiquadratic/ResidueDegree.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Multiquadratic/ResidueDegree.lean#L195)
- [Tau Ceti roadmap status: Multiquadratic fields and genus theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/Multiquadratic/STATUS.md)
