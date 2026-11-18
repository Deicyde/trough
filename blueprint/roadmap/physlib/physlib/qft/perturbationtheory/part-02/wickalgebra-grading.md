---
declaration: module
origin: cited
lean: FieldSpecification.WickAlgebra.statSubmodule, FieldSpecification.WickAlgebra.ofCrAnList_mem_statSubmodule_of_eq, FieldSpecification.WickAlgebra.ofCrAnList_mem_statSubmodule, FieldSpecification.WickAlgebra.mem_bosonic_of_mem_free_bosonic, FieldSpecification.WickAlgebra.mem_fermionic_of_mem_free_fermionic, FieldSpecification.WickAlgebra.mem_statSubmodule_of_mem_statisticSubmodule, FieldSpecification.WickAlgebra.ιStateSubmodule, FieldSpecification.WickAlgebra.bosonicProjFree
statement: formalized
proof: formalized
---

# Grading on the field operation algebra

The module `Physlib.QFT.PerturbationTheory.WickAlgebra.Grading`, [Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean): 38 declarations, 7 with a docstring.

**`FieldSpecification.WickAlgebra.statSubmodule`**, a def, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L26).

> The submodule of `𝓕.WickAlgebra` spanned by lists of field statistic `f`.

```lean
def statSubmodule (f : FieldStatistic) : Submodule ℂ 𝓕.WickAlgebra
```

**`FieldSpecification.WickAlgebra.ofCrAnList_mem_statSubmodule_of_eq`**, a lemma, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L29).

```lean
lemma ofCrAnList_mem_statSubmodule_of_eq (φs : List 𝓕.CrAnFieldOp) (f : FieldStatistic)
    (h : (𝓕 |>ₛ φs) = f) : ofCrAnList φs ∈ statSubmodule f
```

**`FieldSpecification.WickAlgebra.ofCrAnList_mem_statSubmodule`**, a lemma, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L33).

```lean
lemma ofCrAnList_mem_statSubmodule (φs : List 𝓕.CrAnFieldOp) :
    ofCrAnList φs ∈ statSubmodule (𝓕 |>ₛ φs)
```

**`FieldSpecification.WickAlgebra.mem_bosonic_of_mem_free_bosonic`**, a lemma, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L37).

```lean
lemma mem_bosonic_of_mem_free_bosonic (a : 𝓕.FieldOpFreeAlgebra)
    (h : a ∈ statisticSubmodule bosonic) : ι a ∈ statSubmodule .bosonic
```

**`FieldSpecification.WickAlgebra.mem_fermionic_of_mem_free_fermionic`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L58).

```lean
lemma mem_fermionic_of_mem_free_fermionic (a : 𝓕.FieldOpFreeAlgebra)
    (h : a ∈ statisticSubmodule fermionic) : ι a ∈ statSubmodule .fermionic
```

**`FieldSpecification.WickAlgebra.mem_statSubmodule_of_mem_statisticSubmodule`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L79).

```lean
lemma mem_statSubmodule_of_mem_statisticSubmodule (f : FieldStatistic) (a : 𝓕.FieldOpFreeAlgebra)
    (h : a ∈ statisticSubmodule f) : ι a ∈ statSubmodule f
```

**`FieldSpecification.WickAlgebra.ιStateSubmodule`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L87).

> The projection of `statisticSubmodule (𝓕 := 𝓕) f` defined in the free algebra to
> `statSubmodule (𝓕 := 𝓕) f`.

```lean
def ιStateSubmodule (f : FieldStatistic) :
    statisticSubmodule (𝓕 := 𝓕) f →ₗ[ℂ] statSubmodule (𝓕 := 𝓕) f
```

## Defining bosonicProj

**`FieldSpecification.WickAlgebra.bosonicProjFree`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L102).

> The projection of `𝓕.FieldOpFreeAlgebra` to `statSubmodule (𝓕 := 𝓕) bosonic`.

```lean
def bosonicProjFree : 𝓕.FieldOpFreeAlgebra →ₗ[ℂ] statSubmodule (𝓕 := 𝓕) bosonic
```

**`FieldSpecification.WickAlgebra.bosonicProjFree_eq_ι_bosonicProjF`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L105).

```lean
lemma bosonicProjFree_eq_ι_bosonicProjF (a : 𝓕.FieldOpFreeAlgebra) :
    (bosonicProjFree a).1 = ι (bosonicProjF a)
```

**`FieldSpecification.WickAlgebra.bosonicProjFree_zero_of_ι_zero`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L108).

```lean
lemma bosonicProjFree_zero_of_ι_zero (a : 𝓕.FieldOpFreeAlgebra) (h : ι a = 0) :
    bosonicProjFree a = 0
```

**`FieldSpecification.WickAlgebra.bosonicProjFree_eq_of_equiv`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L115).

```lean
lemma bosonicProjFree_eq_of_equiv (a b : 𝓕.FieldOpFreeAlgebra) (h : a ≈ b) :
    bosonicProjFree a = bosonicProjFree b
```

**`FieldSpecification.WickAlgebra.bosonicProj`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L123).

> The projection of `𝓕.WickAlgebra` to `statSubmodule (𝓕 := 𝓕) bosonic`.

```lean
def bosonicProj : 𝓕.WickAlgebra →ₗ[ℂ] statSubmodule (𝓕 := 𝓕) bosonic
```

**`FieldSpecification.WickAlgebra.bosonicProj_eq_bosonicProjFree`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L138).

```lean
lemma bosonicProj_eq_bosonicProjFree (a : 𝓕.FieldOpFreeAlgebra) :
    bosonicProj (ι a) = bosonicProjFree a
```

## Defining fermionicProj

**`FieldSpecification.WickAlgebra.fermionicProjFree`**, a def, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L148).

> The projection of `𝓕.FieldOpFreeAlgebra` to `statSubmodule (𝓕 := 𝓕) fermionic`.

```lean
def fermionicProjFree : 𝓕.FieldOpFreeAlgebra →ₗ[ℂ] statSubmodule (𝓕 := 𝓕) fermionic
```

**`FieldSpecification.WickAlgebra.fermionicProjFree_eq_ι_fermionicProjF`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L151).

```lean
lemma fermionicProjFree_eq_ι_fermionicProjF (a : 𝓕.FieldOpFreeAlgebra) :
    (fermionicProjFree a).1 = ι (fermionicProjF a)
```

**`FieldSpecification.WickAlgebra.fermionicProjFree_zero_of_ι_zero`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L154).

```lean
lemma fermionicProjFree_zero_of_ι_zero (a : 𝓕.FieldOpFreeAlgebra) (h : ι a = 0) :
    fermionicProjFree a = 0
```

**`FieldSpecification.WickAlgebra.fermionicProjFree_eq_of_equiv`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L161).

```lean
lemma fermionicProjFree_eq_of_equiv (a b : 𝓕.FieldOpFreeAlgebra) (h : a ≈ b) :
    fermionicProjFree a = fermionicProjFree b
```

**`FieldSpecification.WickAlgebra.fermionicProj`**, a def, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L169).

> The projection of `𝓕.WickAlgebra` to `statSubmodule (𝓕 := 𝓕) fermionic`.

```lean
def fermionicProj : 𝓕.WickAlgebra →ₗ[ℂ] statSubmodule (𝓕 := 𝓕) fermionic
```

**`FieldSpecification.WickAlgebra.fermionicProj_eq_fermionicProjFree`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L184).

```lean
lemma fermionicProj_eq_fermionicProjFree (a : 𝓕.FieldOpFreeAlgebra) :
    fermionicProj (ι a) = fermionicProjFree a
```

## Interaction between bosonicProj and fermionicProj

**`FieldSpecification.WickAlgebra.bosonicProj_add_fermionicProj`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L193).

```lean
lemma bosonicProj_add_fermionicProj (a : 𝓕.WickAlgebra) :
    bosonicProj a + (fermionicProj a).1 = a
```

**`FieldSpecification.WickAlgebra.bosonicProj_mem_bosonic`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L201).

```lean
lemma bosonicProj_mem_bosonic (a : 𝓕.WickAlgebra) (ha : a ∈ statSubmodule .bosonic) :
    bosonicProj a = ⟨a, ha⟩
```

**`FieldSpecification.WickAlgebra.fermionicProj_mem_fermionic`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L225).

```lean
lemma fermionicProj_mem_fermionic (a : 𝓕.WickAlgebra) (ha : a ∈ statSubmodule .fermionic) :
    fermionicProj a = ⟨a, ha⟩
```

**`FieldSpecification.WickAlgebra.bosonicProj_mem_fermionic`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L248).

```lean
lemma bosonicProj_mem_fermionic (a : 𝓕.WickAlgebra) (ha : a ∈ statSubmodule .fermionic) :
    bosonicProj a = 0
```

**`FieldSpecification.WickAlgebra.fermionicProj_mem_bosonic`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L254).

```lean
lemma fermionicProj_mem_bosonic (a : 𝓕.WickAlgebra) (ha : a ∈ statSubmodule .bosonic) :
    fermionicProj a = 0
```

**`FieldSpecification.WickAlgebra.mem_bosonic_iff_fermionicProj_eq_zero`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L260).

```lean
lemma mem_bosonic_iff_fermionicProj_eq_zero (a : 𝓕.WickAlgebra) :
    a ∈ statSubmodule bosonic ↔ fermionicProj a = 0
```

**`FieldSpecification.WickAlgebra.mem_fermionic_iff_bosonicProj_eq_zero`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L272).

```lean
lemma mem_fermionic_iff_bosonicProj_eq_zero (a : 𝓕.WickAlgebra) :
    a ∈ statSubmodule fermionic ↔ bosonicProj a = 0
```

**`FieldSpecification.WickAlgebra.eq_zero_of_bosonic_and_fermionic`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L284).

```lean
lemma eq_zero_of_bosonic_and_fermionic {a : 𝓕.WickAlgebra}
    (hb : a ∈ statSubmodule bosonic) (hf : a ∈ statSubmodule fermionic) : a = 0
```

**`FieldSpecification.WickAlgebra.bosonicProj_fermionicProj_eq_zero`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L293).

```lean
lemma bosonicProj_fermionicProj_eq_zero (a : 𝓕.WickAlgebra) :
    bosonicProj (fermionicProj a).1 = 0
```

**`FieldSpecification.WickAlgebra.fermionicProj_bosonicProj_eq_zero`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L299).

```lean
lemma fermionicProj_bosonicProj_eq_zero (a : 𝓕.WickAlgebra) :
    fermionicProj (bosonicProj a).1 = 0
```

**`FieldSpecification.WickAlgebra.bosonicProj_bosonicProj_eq_bosonicProj`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L305).

```lean
lemma bosonicProj_bosonicProj_eq_bosonicProj (a : 𝓕.WickAlgebra) :
    bosonicProj (bosonicProj a).1 = bosonicProj a
```

**`FieldSpecification.WickAlgebra.fermionicProj_fermionicProj_eq_fermionicProj`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L310).

```lean
lemma fermionicProj_fermionicProj_eq_fermionicProj (a : 𝓕.WickAlgebra) :
    fermionicProj (fermionicProj a).1 = fermionicProj a
```

**`FieldSpecification.WickAlgebra.bosonicProj_of_bosonic_part`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L315).

```lean
lemma bosonicProj_of_bosonic_part
    (a : DirectSum FieldStatistic (fun i => (statSubmodule (𝓕 := 𝓕) i))) :
    bosonicProj (a bosonic).1 = (a bosonic)
```

**`FieldSpecification.WickAlgebra.bosonicProj_of_fermionic_part`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L321).

```lean
lemma bosonicProj_of_fermionic_part
    (a : DirectSum FieldStatistic (fun i => (statSubmodule (𝓕 := 𝓕) i))) :
    bosonicProj (a fermionic).1 = 0
```

**`FieldSpecification.WickAlgebra.fermionicProj_of_bosonic_part`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L328).

```lean
lemma fermionicProj_of_bosonic_part
    (a : DirectSum FieldStatistic (fun i => (statSubmodule (𝓕 := 𝓕) i))) :
    fermionicProj (a bosonic).1 = 0
```

**`FieldSpecification.WickAlgebra.fermionicProj_of_fermionic_part`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L335).

```lean
lemma fermionicProj_of_fermionic_part
    (a : DirectSum FieldStatistic (fun i => (statSubmodule (𝓕 := 𝓕) i))) :
    fermionicProj (a fermionic).1 = (a fermionic)
```

## The grading

**`FieldSpecification.WickAlgebra.coeAddMonoidHom_apply_eq_bosonic_plus_fermionic`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L346).

```lean
lemma coeAddMonoidHom_apply_eq_bosonic_plus_fermionic
    (a : DirectSum FieldStatistic (fun i => (statSubmodule (𝓕 := 𝓕) i))) :
    DirectSum.coeAddMonoidHom statSubmodule a = a.1 bosonic + a.1 fermionic
```

**`FieldSpecification.WickAlgebra.directSum_eq_bosonic_plus_fermionic`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L364).

```lean
lemma directSum_eq_bosonic_plus_fermionic
    (a : DirectSum FieldStatistic (fun i => (statSubmodule (𝓕 := 𝓕) i))) :
    a = (DirectSum.of (fun i => ↥(statSubmodule (𝓕 := 𝓕) i)) bosonic) (a bosonic) +
    (DirectSum.of (fun i => ↥(statSubmodule (𝓕 := 𝓕) i)) fermionic) (a fermionic)
```

**`FieldSpecification.WickAlgebra.WickAlgebraGrade`**, an instance, [line 398](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean#L398).

> For a field specification `𝓕`, the algebra `𝓕.WickAlgebra` is graded by `FieldStatistic`.
> Those `ofCrAnList φs` for which `φs` has an overall `bosonic` statistic
> (i.e. `𝓕 |>ₛ φs = bosonic`) span `bosonic`
> submodule, whilst those `ofCrAnList φs` for which `φs` has an overall `fermionic` statistic
> (i.e. `𝓕 |>ₛ φs = fermionic`) span the `fermionic` submodule.

```lean
instance WickAlgebraGrade : GradedAlgebra (A := 𝓕.WickAlgebra) statSubmodule
```

## Depends on

- [The Wick Algebra](wickalgebra-basic.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/Grading.lean)
