---
declaration: theorem
origin: cited
lean: Homogeneous.homogeneousSpace_exists_inj_tendsto, Homogeneous.homogeneousSpace_exists_surjective, Homogeneous.firstCountableTopology_of_countablyMonolithicSpace, Homogeneous.countablyMonolithicSpace_card_lt, Homogeneous.monolithicSpace_exists_nhds_generated_countable
statement: formalized
---

# Conjectures around homogeneous topological spaces

> This file formalizes the notions of a homogeneous topological space and of (ω-)monolithic
> topological spaces, and states some open problems about homogeneous and monolithic compact spaces.
>
> *References:*
> * [Ar2013] Arhangeliski, Alexandr. "Selected old open problems in general topology."
>   Buletinul Academiei de Ştiinţe a Republicii Moldova. Matematica 73.2-3 (2013): 37-46.
>   https://www.math.md/files/basm/y2013-n2-3/y2013-n2-3-(pp37-46).pdf.pdf
> * [Ar1987] Arhangel'skii, A. V. "Topological homogeneity. Topological groups and their continuous
>   images." Russian Mathematical Surveys 42.2 (1987): 83-131.
>   https://doi.org/10.1070/RM1987v042n02ABEH001333

*Quoted from [FormalConjectures/Paper/Homogenous.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Homogenous.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 5 open. It also has 5 test statements, counted here but not shown.

## `Homogeneous.homogeneousSpace_exists_inj_tendsto`

Open: stated without proof.

> Problem 13 in [Ar2013]:
> Is it true that every infinite homogeneous compact hausdorff
> space contains a non-trivial convergent sequence?

```lean
theorem homogeneousSpace_exists_inj_tendsto :
    ∀ (X : Type) (_ : TopologicalSpace X), ¬ Finite X → T2Space X → CompactSpace X →
      HomogeneousSpace X → ∃ s : ℕ → X, s.Injective ∧ ∃ a : X, Tendsto s atTop (nhds a)
```

Category `research open`; AMS [54 General topology](../../by-subject/part-02/54-general-topology/README.md). Declared in [FormalConjectures/Paper/Homogenous.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Homogenous.lean#L63).

## `Homogeneous.homogeneousSpace_exists_surjective`

Open: stated without proof.

> Problem 14 in [Ar2013]:
> Is it possible to represent an arbitrary compact hausdorff space as an image
> of a homogeneous compact space under a continuous mapping?

```lean
theorem homogeneousSpace_exists_surjective :
    ∀ (X : Type) (_ : TopologicalSpace X), T2Space X → CompactSpace X →
      ∃ (Y : Type) (_ : TopologicalSpace Y), T2Space Y ∧ CompactSpace Y ∧ HomogeneousSpace Y ∧
        ∃ f : Y → X, Continuous f ∧ f.Surjective
```

Category `research open`; AMS [54 General topology](../../by-subject/part-02/54-general-topology/README.md). Declared in [FormalConjectures/Paper/Homogenous.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Homogenous.lean#L72).

## `Homogeneous.firstCountableTopology_of_countablyMonolithicSpace`

Open: stated without proof.

> Problem 15 in [Ar2013]:
> Is every homogeneous ω-monolithic compact hausdorff space first countable?

```lean
theorem firstCountableTopology_of_countablyMonolithicSpace :
    ∀ (X : Type) (_ : TopologicalSpace X), T2Space X → CompactSpace X →
      HomogeneousSpace X → CountablyMonolithicSpace X → FirstCountableTopology X
```

Category `research open`; AMS [54 General topology](../../by-subject/part-02/54-general-topology/README.md). Declared in [FormalConjectures/Paper/Homogenous.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Homogenous.lean#L94).

## `Homogeneous.countablyMonolithicSpace_card_lt`

Open: stated without proof.

> Problem 16 in [Ar2013]:
> Is the cardinality of every homogeneous ω-monolithic compact hausdorff space not greater than 𝔠?

```lean
theorem countablyMonolithicSpace_card_lt :
    ∀ (X : Type) (_ : TopologicalSpace X), T2Space X → CompactSpace X →
      HomogeneousSpace X → CountablyMonolithicSpace X → #X ≤ 𝔠
```

Category `research open`; AMS [54 General topology](../../by-subject/part-02/54-general-topology/README.md). Declared in [FormalConjectures/Paper/Homogenous.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Homogenous.lean#L102).

## `Homogeneous.monolithicSpace_exists_nhds_generated_countable`

Open: stated without proof.

> Problem 17 in [Ar2013]:
> Is it true that every nonempty monolithic compact hausdorff space contains a point with a
> first countable neighborhood basis?
>
> Note: `Nonempty X` is required since the conclusion asserts the existence of a point.

```lean
theorem monolithicSpace_exists_nhds_generated_countable :
    ∀ (X : Type) (_ : TopologicalSpace X), T2Space X → CompactSpace X →
      Nonempty X → MonolithicSpace X → ∃ x : X, (𝓝 x).IsCountablyGenerated
```

Category `research open`; AMS [54 General topology](../../by-subject/part-02/54-general-topology/README.md). Declared in [FormalConjectures/Paper/Homogenous.lean, line 152](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Homogenous.lean#L152).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/Homogenous.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Homogenous.lean)
- [https://www.math.md/files/basm/y2013-n2-3/y2013-n2-3-(pp37-46](https://www.math.md/files/basm/y2013-n2-3/y2013-n2-3-%28pp37-46)
