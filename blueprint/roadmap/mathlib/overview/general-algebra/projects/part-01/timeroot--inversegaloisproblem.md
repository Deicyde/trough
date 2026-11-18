---
declaration: theorem
origin: cited
lean: Shafarevich.splitPrimePowerEP, Rigidity.RET.IsRegularInverseGalois.of_commGroup, isRegularInverseGalois_of_isSemiabelian, InverseGalois.isRegularInverseGalois_of_isZGroup, InverseGalois.isRegularInverseGalois_of_nilpotencyClass_le_two, InverseGalois.isRegularInverseGalois_of_forall_sylow_comm, InverseGalois.isRegularInverseGalois_of_card_lt_fortyeight, InverseGalois.isRegularInverseGalois_sylow_perm
statement: formalized
proof: formalized
---

# The Inverse Galois Problem, in Lean 4

[Timeroot/InverseGaloisProblem](https://github.com/Timeroot/InverseGaloisProblem) at commit [973f72c1](https://github.com/Timeroot/InverseGaloisProblem/tree/973f72c1900fb72c460833448b472899fa659366), 2026-09-16.

## Depends on

- [Group](../../group-theory/part-01/group.md)
- [Nilpotent group](../../group-theory/part-01/nilpotent-group.md)
- [Subgroup](../../group-theory/part-01/subgroup.md)
- [Permutation group of a type](../../group-theory/part-02/permutation-group-of-a-type.md)

## Proof depends on

- [Eisenstein's criterion](../../polynomials-and-power-series/eisensteins-criterion.md)
- [Symmetric polynomials](../../../../undergraduate/ring-theory/polynomial-rings/symmetric-polynomials.md)
- [Relationship between the coefficients and the roots of a split polynomial](../../../../undergraduate/ring-theory/polynomial-rings/relationship-between-the-coefficients-and-the-ro.md)
- [Rolle's theorem](../../../analysis/differentiability/rolles-theorem.md)
- [Wilson’s Lemma](../../../../hundred-theorems/part-02/wilsons-lemma.md)
- [Separable polynomial](../../polynomials-and-power-series/separable-polynomial.md)
- [Galois correspondence](../../field-theory/galois-correspondence.md)
- [Wedderburn's little theorem](../../../../thousand-plus/algebra/13-commutative-algebra/wedderburns-little-theorem.md)

## Main results

Its Lean names are 8 of the 17 theorems its README names in code:

- [`Shafarevich.splitPrimePowerEP`](https://github.com/Timeroot/InverseGaloisProblem/blob/973f72c1900fb72c460833448b472899fa659366/InverseGalois/Solvable/Shafarevich/Theorem.lean#L44) (theorem)
- [`Rigidity.RET.IsRegularInverseGalois.of_commGroup`](https://github.com/Timeroot/InverseGaloisProblem/blob/973f72c1900fb72c460833448b472899fa659366/InverseGalois/Rigidity/RET/AbelFinale.lean#L73) (theorem)
- [`isRegularInverseGalois_of_isSemiabelian`](https://github.com/Timeroot/InverseGaloisProblem/blob/973f72c1900fb72c460833448b472899fa659366/InverseGalois/Rigidity/RET/Wreath/Main.lean#L221) (theorem)
- [`InverseGalois.isRegularInverseGalois_of_isZGroup`](https://github.com/Timeroot/InverseGaloisProblem/blob/973f72c1900fb72c460833448b472899fa659366/InverseGalois/Rigidity/RET/Wreath/SmallGroups.lean#L88) (theorem)
- [`InverseGalois.isRegularInverseGalois_of_nilpotencyClass_le_two`](https://github.com/Timeroot/InverseGaloisProblem/blob/973f72c1900fb72c460833448b472899fa659366/InverseGalois/Rigidity/RET/Wreath/SmallGroups.lean#L247) (theorem)
- [`InverseGalois.isRegularInverseGalois_of_forall_sylow_comm`](https://github.com/Timeroot/InverseGaloisProblem/blob/973f72c1900fb72c460833448b472899fa659366/InverseGalois/Rigidity/RET/Wreath/SmallGroups.lean#L189) (theorem)
- [`InverseGalois.isRegularInverseGalois_of_card_lt_fortyeight`](https://github.com/Timeroot/InverseGaloisProblem/blob/973f72c1900fb72c460833448b472899fa659366/InverseGalois/Rigidity/RET/Wreath/SmallGroups.lean#L164) (theorem)
- [`InverseGalois.isRegularInverseGalois_sylow_perm`](https://github.com/Timeroot/InverseGaloisProblem/blob/973f72c1900fb72c460833448b472899fa659366/InverseGalois/Rigidity/RET/Wreath/SmallGroups.lean#L217) (theorem)

No file its headlines import, directly or not (1026 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.28.0, Mathlib at [8f9d9cff](https://github.com/leanprover-community/mathlib4/tree/8f9d9cff6bd728b17a24e163c9402775d9e6a365).
- 2,014 .lean files; its Lean libraries `InverseGalois`, `Mathieu`, `MathieuRigidity`, `MathieuRigidityM22`, `MathieuRigidityM24`, `PGL2Large` and 3 more hold 2,014, declaring 21,569 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- No license file; facts only.

## Builds on

- Mathlib, at [8f9d9cff](https://github.com/leanprover-community/mathlib4/tree/8f9d9cff6bd728b17a24e163c9402775d9e6a365).

## Placement

4 of the 4 Mathlib concepts its headline statements name are in General algebra.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: General algebra (61 of 79 imports, 2.2×), Topology (8 of 79 imports, 1.4×). *Proof depends on* names 8 of the 171 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [Timeroot/InverseGaloisProblem at 973f72c1](https://github.com/Timeroot/InverseGaloisProblem/tree/973f72c1900fb72c460833448b472899fa659366)
