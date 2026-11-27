---
declaration: theorem
origin: cited
lean: FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_one, FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_two, FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_three, FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_four, FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_five, FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_six, FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_seven
statement: formalized
proof: formalized
---

# Enumeration of finite integral relation algebras through seven atoms

> Classifies finite integral relation algebras by lawful atom cycles and verifies the published isomorphism-class counts using Burnside's lemma and kernel-checked Boolean counting certificates. The reference table is Peter Jipsen's compilation, which follows the ordering of Roger Maddux's earlier list.

*Quoted from the card [LeanPool/projects/finite-integral-relation-algebras.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/finite-integral-relation-algebras.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 7 main results, each with its informal statement quoted from the card. The scan finds 7 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_one`](https://leanpool.github.io/lean-pool/LeanPool/FiniteIntegralRelationAlgebras/Atoms1/Total.html#FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_one) (theorem; a main declaration), declared in [LeanPool/FiniteIntegralRelationAlgebras/Atoms1/Total.lean, line 19](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FiniteIntegralRelationAlgebras/Atoms1/Total.lean#L19): “There is one isomorphism class of finite integral relation algebras with exactly one atom.”
- [`FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_two`](https://leanpool.github.io/lean-pool/LeanPool/FiniteIntegralRelationAlgebras/Atoms2/Total.html#FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_two) (theorem; a main declaration), declared in [LeanPool/FiniteIntegralRelationAlgebras/Atoms2/Total.lean, line 19](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FiniteIntegralRelationAlgebras/Atoms2/Total.lean#L19): “There are 2 isomorphism classes of finite integral relation algebras with exactly two atoms.”
- [`FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_three`](https://leanpool.github.io/lean-pool/LeanPool/FiniteIntegralRelationAlgebras/Atoms3/Total.html#FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_three) (theorem; a main declaration), declared in [LeanPool/FiniteIntegralRelationAlgebras/Atoms3/Total.lean, line 20](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FiniteIntegralRelationAlgebras/Atoms3/Total.lean#L20): “There are 10 isomorphism classes of finite integral relation algebras with exactly three atoms.”
- [`FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_four`](https://leanpool.github.io/lean-pool/LeanPool/FiniteIntegralRelationAlgebras/Atoms4/Total.html#FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_four) (theorem; a main declaration), declared in [LeanPool/FiniteIntegralRelationAlgebras/Atoms4/Total.lean, line 20](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FiniteIntegralRelationAlgebras/Atoms4/Total.lean#L20): “There are 102 isomorphism classes of finite integral relation algebras with exactly four atoms.”
- [`FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_five`](https://leanpool.github.io/lean-pool/LeanPool/FiniteIntegralRelationAlgebras/Atoms5/Total.html#FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_five) (theorem; a main declaration), declared in [LeanPool/FiniteIntegralRelationAlgebras/Atoms5/Total.lean, line 21](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FiniteIntegralRelationAlgebras/Atoms5/Total.lean#L21): “There are 4,412 isomorphism classes of finite integral relation algebras with exactly five atoms.”
- [`FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_six`](https://leanpool.github.io/lean-pool/LeanPool/FiniteIntegralRelationAlgebras/Atoms6/Total.html#FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_six) (theorem; a main declaration), declared in [LeanPool/FiniteIntegralRelationAlgebras/Atoms6/Total.lean, line 21](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FiniteIntegralRelationAlgebras/Atoms6/Total.lean#L21): “There are 4,886,349 isomorphism classes of finite integral relation algebras with exactly six atoms.”
- [`FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_seven`](https://leanpool.github.io/lean-pool/LeanPool/FiniteIntegralRelationAlgebras/Atoms7/Total.html#FiniteIntegralRelationAlgebras.RelationAlgebra.IntegralAtom.IsoClass.card_ofAtoms_seven) (theorem; a main declaration), declared in [LeanPool/FiniteIntegralRelationAlgebras/Atoms7/Total.lean, line 22](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FiniteIntegralRelationAlgebras/Atoms7/Total.lean#L22): “There are 344,809,166,311 isomorphism classes of finite integral relation algebras with exactly seven atoms.”

## Project

- Authors: Chris Henson.
- Source: *List of small integral relation algebras* by Peter Jipsen, [https://www1.chapman.edu/~jipsen/gap/ramaddux.html](https://www1.chapman.edu/~jipsen/gap/ramaddux.html).
- Project repository: [chenson2018/finite-integral-ra](https://github.com/chenson2018/finite-integral-ra), at commit [5620a22c](https://github.com/chenson2018/finite-integral-ra/tree/5620a22cc48127b592bca85b1aaf013e55d4f6df).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 03G15, 05A15, 68V20.
- In Lean Pool: [LeanPool/FiniteIntegralRelationAlgebras](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FiniteIntegralRelationAlgebras), from the card [LeanPool/projects/finite-integral-relation-algebras.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/finite-integral-relation-algebras.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/finite-integral-relation-algebras.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/finite-integral-relation-algebras.yaml)
- [Lean Pool at bb99e52c: LeanPool/FiniteIntegralRelationAlgebras](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/FiniteIntegralRelationAlgebras)
