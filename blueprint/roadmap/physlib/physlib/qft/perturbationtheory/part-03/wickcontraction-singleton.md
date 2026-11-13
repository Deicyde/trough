---
declaration: module
origin: cited
lean: WickContraction.singleton, WickContraction.mem_singleton, WickContraction.mem_singleton_iff, WickContraction.of_singleton_eq, WickContraction.singleton_prod, WickContraction.singleton_fstFieldOfContract, WickContraction.singleton_sndFieldOfContract, WickContraction.singleton_sign_expand
statement: formalized
proof: formalized
---

# Singleton of contractions

The module `Physlib.QFT.PerturbationTheory.WickContraction.Singleton`, [Physlib/QFT/PerturbationTheory/WickContraction/Singleton.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Singleton.lean): 15 declarations, 1 with a docstring.

**`WickContraction.singleton`**, a def, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Singleton.lean#L30).

> The Wick contraction formed from a single ordered pair.

```lean
def singleton {i j : Fin n} (hij : i < j) : WickContraction n
```

**`WickContraction.mem_singleton`**, a lemma, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Singleton.lean#L42).

```lean
lemma mem_singleton {i j : Fin n} (hij : i < j) :
    {i, j} ∈ (singleton hij).1
```

**`WickContraction.mem_singleton_iff`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Singleton.lean#L46).

```lean
lemma mem_singleton_iff {i j : Fin n} (hij : i < j) {a : Finset (Fin n)} :
    a ∈ (singleton hij).1 ↔ a = {i, j}
```

**`WickContraction.of_singleton_eq`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Singleton.lean#L50).

```lean
lemma of_singleton_eq {i j : Fin n} (hij : i < j) (a : (singleton hij).1) :
    a = ⟨{i, j}, mem_singleton hij⟩
```

**`WickContraction.singleton_prod`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Singleton.lean#L57).

```lean
lemma singleton_prod {φs : List 𝓕.FieldOp} {i j : Fin φs.length} (hij : i < j)
    (f : (singleton hij).1 → M) [CommMonoid M] :
    ∏ a, f a = f ⟨{i,j}, mem_singleton hij⟩
```

**`WickContraction.singleton_fstFieldOfContract`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Singleton.lean#L64).

```lean
lemma singleton_fstFieldOfContract {i j : Fin n} (hij : i < j) :
    (singleton hij).fstFieldOfContract ⟨{i, j}, mem_singleton hij⟩ = i
```

**`WickContraction.singleton_sndFieldOfContract`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Singleton.lean#L72).

```lean
lemma singleton_sndFieldOfContract {i j : Fin n} (hij : i < j) :
    (singleton hij).sndFieldOfContract ⟨{i, j}, mem_singleton hij⟩ = j
```

**`WickContraction.singleton_sign_expand`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Singleton.lean#L79).

```lean
lemma singleton_sign_expand {φs : List 𝓕.FieldOp} {i j : Fin φs.length} (hij : i < j) :
    (singleton hij).sign = 𝓢(𝓕 |>ₛ φs[j], 𝓕 |>ₛ ⟨φs.get, (singleton hij).signFinset i j⟩)
```

**`WickContraction.singleton_getDual?_eq_none_iff_neq`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Singleton.lean#L84).

```lean
lemma singleton_getDual?_eq_none_iff_neq {i j : Fin n} (hij : i < j) (a : Fin n) :
    (singleton hij).getDual? a = none ↔ (i ≠ a ∧ j ≠ a)
```

**`WickContraction.singleton_uncontractedEmd_ne_left`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Singleton.lean#L91).

```lean
lemma singleton_uncontractedEmd_ne_left {φs : List 𝓕.FieldOp} {i j : Fin φs.length} (hij : i < j)
    (a : Fin [singleton hij]ᵘᶜ.length) :
    (singleton hij).uncontractedListEmd a ≠ i
```

**`WickContraction.singleton_uncontractedEmd_ne_right`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Singleton.lean#L102).

```lean
lemma singleton_uncontractedEmd_ne_right {φs : List 𝓕.FieldOp} {i j : Fin φs.length} (hij : i < j)
    (a : Fin [singleton hij]ᵘᶜ.length) :
    (singleton hij).uncontractedListEmd a ≠ j
```

**`WickContraction.mem_signFinset`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Singleton.lean#L114).

```lean
lemma mem_signFinset {i j : Fin n} (hij : i < j) (a : Fin n) :
    a ∈ (singleton hij).signFinset i j ↔ i < a ∧ a < j
```

**`WickContraction.subContraction_singleton_eq_singleton`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Singleton.lean#L123).

```lean
lemma subContraction_singleton_eq_singleton {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length)
    (a : φsΛ.1) : φsΛ.subContraction {a.1} (by simp) =
    singleton (φsΛ.fstFieldOfContract_lt_sndFieldOfContract a)
```

**`WickContraction.singleton_timeContract`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Singleton.lean#L131).

```lean
lemma singleton_timeContract {φs : List 𝓕.FieldOp} {i j : Fin φs.length} (hij : i < j) :
    (singleton hij).timeContract =
    ⟨WickAlgebra.timeContract φs[i] φs[j], timeContract_mem_center _ _⟩
```

**`WickContraction.singleton_staticContract`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Singleton.lean#L137).

```lean
lemma singleton_staticContract {φs : List 𝓕.FieldOp} {i j : Fin φs.length} (hij : i < j) :
    (singleton hij).staticContract.1 =
    [anPart φs[i], ofFieldOp φs[j]]ₛ
```

## Depends on

- [Sign associated with a contraction](wickcontraction-sign-basic.md)
- [Time contractions](wickcontraction-staticcontract.md)
- [Sub contractions](wickcontraction-subcontraction.md)
- [Time contractions](wickcontraction-timecontract.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/Singleton.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Singleton.lean)
