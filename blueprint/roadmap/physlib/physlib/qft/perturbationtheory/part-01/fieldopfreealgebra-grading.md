---
declaration: module
origin: cited
lean: FieldSpecification.FieldOpFreeAlgebra.statisticSubmodule, FieldSpecification.FieldOpFreeAlgebra.ofCrAnListF_mem_statisticSubmodule_of, FieldSpecification.FieldOpFreeAlgebra.ofCrAnListF_bosonic_or_fermionic, FieldSpecification.FieldOpFreeAlgebra.ofCrAnOpF_bosonic_or_fermionic, FieldSpecification.FieldOpFreeAlgebra.bosonicProjF, FieldSpecification.FieldOpFreeAlgebra.bosonicProjF_ofCrAnListF, FieldSpecification.FieldOpFreeAlgebra.bosonicProjF_of_mem_bosonic, FieldSpecification.FieldOpFreeAlgebra.bosonicProjF_of_mem_fermionic
statement: formalized
proof: formalized
---

# Grading on the FieldOpFreeAlgebra

The module `Physlib.QFT.PerturbationTheory.FieldOpFreeAlgebra.Grading`, [Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean): 24 declarations, 4 with a docstring.

**`FieldSpecification.FieldOpFreeAlgebra.statisticSubmodule`**, a def, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L27).

> The submodule of `FieldOpFreeAlgebra` spanned by lists of field statistic `f`.

```lean
def statisticSubmodule (f : FieldStatistic) : Submodule ℂ 𝓕.FieldOpFreeAlgebra
```

**`FieldSpecification.FieldOpFreeAlgebra.ofCrAnListF_mem_statisticSubmodule_of`**, a lemma, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L30).

```lean
lemma ofCrAnListF_mem_statisticSubmodule_of (φs : List 𝓕.CrAnFieldOp) (f : FieldStatistic)
    (h : (𝓕 |>ₛ φs) = f) :
    ofCrAnListF φs ∈ statisticSubmodule f
```

**`FieldSpecification.FieldOpFreeAlgebra.ofCrAnListF_bosonic_or_fermionic`**, a lemma, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L35).

```lean
lemma ofCrAnListF_bosonic_or_fermionic (φs : List 𝓕.CrAnFieldOp) :
    ofCrAnListF φs ∈ statisticSubmodule bosonic ∨
    ofCrAnListF φs ∈ statisticSubmodule fermionic
```

**`FieldSpecification.FieldOpFreeAlgebra.ofCrAnOpF_bosonic_or_fermionic`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L44).

```lean
lemma ofCrAnOpF_bosonic_or_fermionic (φ : 𝓕.CrAnFieldOp) :
    ofCrAnOpF φ ∈ statisticSubmodule bosonic ∨ ofCrAnOpF φ ∈ statisticSubmodule fermionic
```

**`FieldSpecification.FieldOpFreeAlgebra.bosonicProjF`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L50).

> The projection of an element of `FieldOpFreeAlgebra` onto it's bosonic part.

```lean
def bosonicProjF : 𝓕.FieldOpFreeAlgebra →ₗ[ℂ] statisticSubmodule (𝓕 := 𝓕) bosonic
```

**`FieldSpecification.FieldOpFreeAlgebra.bosonicProjF_ofCrAnListF`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L57).

```lean
lemma bosonicProjF_ofCrAnListF (φs : List 𝓕.CrAnFieldOp) :
    bosonicProjF (ofCrAnListF φs) = if h : (𝓕 |>ₛ φs) = bosonic then
      ⟨ofCrAnListF φs, Submodule.mem_span.mpr fun _ a => a ⟨φs, ⟨rfl, h⟩⟩⟩ else 0
```

**`FieldSpecification.FieldOpFreeAlgebra.bosonicProjF_of_mem_bosonic`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L64).

```lean
lemma bosonicProjF_of_mem_bosonic (a : 𝓕.FieldOpFreeAlgebra) (h : a ∈ statisticSubmodule bosonic) :
    bosonicProjF a = ⟨a, h⟩
```

**`FieldSpecification.FieldOpFreeAlgebra.bosonicProjF_of_mem_fermionic`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L81).

```lean
lemma bosonicProjF_of_mem_fermionic (a : 𝓕.FieldOpFreeAlgebra)
    (h : a ∈ statisticSubmodule fermionic) :
    bosonicProjF a = 0
```

**`FieldSpecification.FieldOpFreeAlgebra.bosonicProjF_of_bonosic_part`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L99).

```lean
lemma bosonicProjF_of_bonosic_part
    (a : DirectSum FieldStatistic (fun i => (statisticSubmodule (𝓕 := 𝓕) i))) :
    bosonicProjF (a bosonic) = a bosonic
```

**`FieldSpecification.FieldOpFreeAlgebra.bosonicProjF_of_fermionic_part`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L105).

```lean
lemma bosonicProjF_of_fermionic_part
    (a : DirectSum FieldStatistic (fun i => (statisticSubmodule (𝓕 := 𝓕) i))) :
    bosonicProjF (a fermionic).1 = 0
```

**`FieldSpecification.FieldOpFreeAlgebra.fermionicProjF`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L112).

> The projection of an element of `FieldOpFreeAlgebra` onto it's fermionic part.

```lean
def fermionicProjF : 𝓕.FieldOpFreeAlgebra →ₗ[ℂ] statisticSubmodule (𝓕 := 𝓕) fermionic
```

**`FieldSpecification.FieldOpFreeAlgebra.fermionicProjF_ofCrAnListF`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L119).

```lean
lemma fermionicProjF_ofCrAnListF (φs : List 𝓕.CrAnFieldOp) :
    fermionicProjF (ofCrAnListF φs) = if h : (𝓕 |>ₛ φs) = fermionic then
      ⟨ofCrAnListF φs, Submodule.mem_span.mpr fun _ a => a ⟨φs, ⟨rfl, h⟩⟩⟩ else 0
```

**`FieldSpecification.FieldOpFreeAlgebra.fermionicProjF_ofCrAnListF_if_bosonic`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L125).

```lean
lemma fermionicProjF_ofCrAnListF_if_bosonic (φs : List 𝓕.CrAnFieldOp) :
    fermionicProjF (ofCrAnListF φs) = if h : (𝓕 |>ₛ φs) = bosonic then
      0 else ⟨ofCrAnListF φs, Submodule.mem_span.mpr fun _ a => a ⟨φs, ⟨rfl,
        by simpa using h⟩⟩⟩
```

**`FieldSpecification.FieldOpFreeAlgebra.fermionicProjF_of_mem_fermionic`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L137).

```lean
lemma fermionicProjF_of_mem_fermionic (a : 𝓕.FieldOpFreeAlgebra)
    (h : a ∈ statisticSubmodule fermionic) :
    fermionicProjF a = ⟨a, h⟩
```

**`FieldSpecification.FieldOpFreeAlgebra.fermionicProjF_of_mem_bosonic`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L155).

```lean
lemma fermionicProjF_of_mem_bosonic (a : 𝓕.FieldOpFreeAlgebra)
    (h : a ∈ statisticSubmodule bosonic) : fermionicProjF a = 0
```

**`FieldSpecification.FieldOpFreeAlgebra.fermionicProjF_of_bosonic_part`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L172).

```lean
lemma fermionicProjF_of_bosonic_part
    (a : DirectSum FieldStatistic (fun i => (statisticSubmodule (𝓕 := 𝓕) i))) :
    fermionicProjF (a bosonic).1 = 0
```

**`FieldSpecification.FieldOpFreeAlgebra.fermionicProjF_of_fermionic_part`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L179).

```lean
lemma fermionicProjF_of_fermionic_part
    (a : DirectSum FieldStatistic (fun i => (statisticSubmodule (𝓕 := 𝓕) i))) :
    fermionicProjF (a fermionic) = a fermionic
```

**`FieldSpecification.FieldOpFreeAlgebra.bosonicProjF_add_fermionicProjF`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L184).

```lean
lemma bosonicProjF_add_fermionicProjF (a : 𝓕.FieldOpFreeAlgebra) :
    a.bosonicProjF + (a.fermionicProjF).1 = a
```

**`FieldSpecification.FieldOpFreeAlgebra.coeAddMonoidHom_apply_eq_bosonic_plus_fermionic`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L199).

```lean
lemma coeAddMonoidHom_apply_eq_bosonic_plus_fermionic
    (a : DirectSum FieldStatistic (fun i => (statisticSubmodule (𝓕 := 𝓕) i))) :
    DirectSum.coeAddMonoidHom statisticSubmodule a = a.1 bosonic + a.1 fermionic
```

**`FieldSpecification.FieldOpFreeAlgebra.directSum_eq_bosonic_plus_fermionic`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L217).

```lean
lemma directSum_eq_bosonic_plus_fermionic
    (a : DirectSum FieldStatistic (fun i => (statisticSubmodule (𝓕 := 𝓕) i))) :
    a = (DirectSum.of (fun i => ↥(statisticSubmodule i)) bosonic) (a bosonic) +
    (DirectSum.of (fun i => ↥(statisticSubmodule i)) fermionic) (a fermionic)
```

**`FieldSpecification.FieldOpFreeAlgebra.fieldOpFreeAlgebraGrade`**, an instance, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L252).

> For a field specification `𝓕`, the algebra `𝓕.FieldOpFreeAlgebra` is graded by `FieldStatistic`.
> Those `ofCrAnListF φs` for which `φs` has an overall `bosonic` statistic
> (i.e. `𝓕 |>ₛ φs = bosonic`) span `bosonic`
> submodule, whilst those `ofCrAnListF φs` for which `φs` has an overall `fermionic` statistic
> (i.e. `𝓕 |>ₛ φs = fermionic`) span
> the `fermionic` submodule.

```lean
instance fieldOpFreeAlgebraGrade :
    GradedAlgebra (A := 𝓕.FieldOpFreeAlgebra) statisticSubmodule
```

**`FieldSpecification.FieldOpFreeAlgebra.eq_zero_of_bosonic_and_fermionic`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L312).

```lean
lemma eq_zero_of_bosonic_and_fermionic {a : 𝓕.FieldOpFreeAlgebra}
    (hb : a ∈ statisticSubmodule bosonic) (hf : a ∈ statisticSubmodule fermionic) : a = 0
```

**`FieldSpecification.FieldOpFreeAlgebra.bosonicProjF_mul`**, a lemma, [line 320](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L320).

```lean
lemma bosonicProjF_mul (a b : 𝓕.FieldOpFreeAlgebra) :
    (a * b).bosonicProjF.1 = a.bosonicProjF.1 * b.bosonicProjF.1
    + a.fermionicProjF.1 * b.fermionicProjF.1
```

**`FieldSpecification.FieldOpFreeAlgebra.fermionicProjF_mul`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean#L369).

```lean
lemma fermionicProjF_mul (a b : 𝓕.FieldOpFreeAlgebra) :
    (a * b).fermionicProjF.1 = a.bosonicProjF.1 * b.fermionicProjF.1
    + a.fermionicProjF.1 * b.bosonicProjF.1
```

## Depends on

- [Creation and annihilation free-algebra](fieldopfreealgebra-basic.md)

## Sources

- [Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/Grading.lean)
