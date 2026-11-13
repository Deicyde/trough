---
declaration: module
origin: cited
lean: PureU1.PermGroup, PureU1.chargeMap, PureU1.permCharges, PureU1.accGrav_invariant, PureU1.accCube_invariant, PureU1.FamilyPermutations, PureU1.FamilyPermutations_charges_apply, PureU1.FamilyPermutations_anomalyFreeLinear_apply
statement: formalized
proof: formalized
---

# Permutations of Pure U(1) ACC

The module `Physlib.QFT.QED.AnomalyCancellation.Permutations`, [Physlib/QFT/QED/AnomalyCancellation/Permutations.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean): 31 declarations (1 instance with no name), 10 with a docstring.

> We define the permutation group action on the charges of the Pure U(1) ACC system.
> We further define the action on the ACC System.

**`PureU1.PermGroup`**, a def, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L27).

> The permutation group of the n-fermions.

```lean
def PermGroup (n : ℕ)
```

**An instance with no name**, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L30).

> The type `PermGroup n` inherits the instance of a group from `Equiv.Perm`.

```lean
instance {n : ℕ} : Group (PermGroup n)
```

**`PureU1.chargeMap`**, a def, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L36).

> The image of an element of `permGroup` under the representation on charges.

```lean
def chargeMap {n : ℕ} (f : PermGroup n) :
    (PureU1 n).Charges →ₗ[ℚ] (PureU1 n).Charges
```

**`PureU1.permCharges`**, a def, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L44).

> The representation of `permGroup` acting on the vector space of charges.

```lean
def permCharges {n : ℕ} : Representation ℚ (PermGroup n) (PureU1 n).Charges
```

**`PureU1.accGrav_invariant`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L49).

```lean
lemma accGrav_invariant {n : ℕ} (f : (PermGroup n)) (S : (PureU1 n).Charges) :
    PureU1.accGrav n (permCharges f S) = accGrav n S
```

**`PureU1.accCube_invariant`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L57).

```lean
lemma accCube_invariant {n : ℕ} (f : (PermGroup n)) (S : (PureU1 n).Charges) :
    accCube n (permCharges f S) = accCube n S
```

**`PureU1.FamilyPermutations`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L68).

> The permutations acting on the ACC system.

```lean
def FamilyPermutations (n : ℕ) : ACCSystemGroupAction (PureU1 n)
```

**`PureU1.FamilyPermutations_charges_apply`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L82).

```lean
lemma FamilyPermutations_charges_apply (S : (PureU1 n).Charges)
    (i : Fin n) (f : (FamilyPermutations n).group) :
    ((FamilyPermutations n).rep f S) i = S (f.invFun i)
```

**`PureU1.FamilyPermutations_anomalyFreeLinear_apply`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L87).

```lean
lemma FamilyPermutations_anomalyFreeLinear_apply (S : (PureU1 n).LinSols)
    (i : Fin n) (f : (FamilyPermutations n).group) :
    ((FamilyPermutations n).linSolRep f S).val i = S.val (f.invFun i)
```

**`PureU1.permOfInjection`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L93).

> A permutation of fermions which takes one ordered subset into another.

```lean
noncomputable def permOfInjection (f g : Fin m ↪ Fin n) : (FamilyPermutations n).group
```

**`PureU1.permTwoInj`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L101).

> Given two distinct elements, an embedding of `Fin 2` into `Fin n`.

```lean
def permTwoInj : Fin 2 ↪ Fin n
```

**`PureU1.permTwoInj_fst`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L108).

```lean
lemma permTwoInj_fst : i ∈ Set.range ⇑(permTwoInj hij)
```

**`PureU1.permTwoInj_fst_apply`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L113).

```lean
lemma permTwoInj_fst_apply :
    (Function.Embedding.toEquivRange (permTwoInj hij)).symm ⟨i, permTwoInj_fst hij⟩ = 0
```

**`PureU1.permTwoInj_snd`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L117).

```lean
lemma permTwoInj_snd : j ∈ Set.range ⇑(permTwoInj hij)
```

**`PureU1.permTwoInj_snd_apply`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L122).

```lean
lemma permTwoInj_snd_apply :
    (Function.Embedding.toEquivRange (permTwoInj hij)).symm
    ⟨j, permTwoInj_snd hij⟩ = 1
```

**`PureU1.permTwo`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L128).

> A permutation which swaps `i` with `i'` and `j` with `j'`.

```lean
noncomputable def permTwo : (FamilyPermutations n).group
```

**`PureU1.permTwo_fst`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L131).

```lean
lemma permTwo_fst : (permTwo hij hij').toFun i' = i
```

**`PureU1.permTwo_snd`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L140).

```lean
lemma permTwo_snd : (permTwo hij hij').toFun j' = j
```

**`PureU1.permThreeInj`**, a def, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L157).

> Given three distinct elements an embedding of `Fin 3` into `Fin n`.

```lean
def permThreeInj : Fin 3 ↪ Fin n
```

**`PureU1.permThreeInj_fst`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L165).

```lean
lemma permThreeInj_fst : i ∈ Set.range ⇑(permThreeInj hij hjk hik)
```

**`PureU1.permThreeInj_fst_apply`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L170).

```lean
lemma permThreeInj_fst_apply :
    (Function.Embedding.toEquivRange (permThreeInj hij hjk hik)).symm
    ⟨i, permThreeInj_fst hij hjk hik⟩ = 0
```

**`PureU1.permThreeInj_snd`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L175).

```lean
lemma permThreeInj_snd : j ∈ Set.range ⇑(permThreeInj hij hjk hik)
```

**`PureU1.permThreeInj_snd_apply`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L180).

```lean
lemma permThreeInj_snd_apply :
    (Function.Embedding.toEquivRange (permThreeInj hij hjk hik)).symm
    ⟨j, permThreeInj_snd hij hjk hik⟩ = 1
```

**`PureU1.permThreeInj_thd`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L185).

```lean
lemma permThreeInj_thd : k ∈ Set.range ⇑(permThreeInj hij hjk hik)
```

**`PureU1.permThreeInj_thd_apply`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L190).

```lean
lemma permThreeInj_thd_apply :
    (Function.Embedding.toEquivRange (permThreeInj hij hjk hik)).symm
    ⟨k, permThreeInj_thd hij hjk hik⟩ = 2
```

**`PureU1.permThree`**, a def, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L196).

> A permutation which swaps three distinct elements with another three.

```lean
noncomputable def permThree : (FamilyPermutations n).group
```

**`PureU1.permThree_fst`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L199).

```lean
lemma permThree_fst : (permThree hij hjk hik hij' hjk' hik').toFun i' = i
```

**`PureU1.permThree_snd`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L208).

```lean
lemma permThree_snd : (permThree hij hjk hik hij' hjk' hik').toFun j' = j
```

**`PureU1.permThree_thd`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L217).

```lean
lemma permThree_thd : (permThree hij hjk hik hij' hjk' hik').toFun k' = k
```

**`PureU1.Prop_two`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L229).

```lean
lemma Prop_two (P : ℚ × ℚ → Prop) {S : (PureU1 n).LinSols}
    {a b : Fin n} (hab : a ≠ b)
    (h : ∀ (f : (FamilyPermutations n).group),
    P ((((FamilyPermutations n).linSolRep f S).val a),
      (((FamilyPermutations n).linSolRep f S).val b))) : ∀ (i j : Fin n) (_ : i ≠ j),
    P (S.val i, S.val j)
```

**`PureU1.Prop_three`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean#L246).

```lean
lemma Prop_three (P : ℚ × ℚ × ℚ → Prop) {S : (PureU1 n).LinSols}
    {a b c : Fin n} (hab : a ≠ b) (hac : a ≠ c) (hbc : b ≠ c)
    (h : ∀ (f : (FamilyPermutations n).group),
    P ((((FamilyPermutations n).linSolRep f S).val a),
      ((((FamilyPermutations n).linSolRep f S).val b),
      (((FamilyPermutations n).linSolRep f S).val c)))) : ∀ (i j k : Fin n)
      (_ : i ≠ j) (_ : j ≠ k) (_ : i ≠ k), P (S.val i, (S.val j, S.val k))
```

## Depends on

- [Group actions on ACC systems.](../anomalycancellation/groupactions.md)
- [Anomaly cancellation of a theory with a pure U(1)-gauge group](anomalycancellation-basic.md)

## Sources

- [Physlib/QFT/QED/AnomalyCancellation/Permutations.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Permutations.lean)
