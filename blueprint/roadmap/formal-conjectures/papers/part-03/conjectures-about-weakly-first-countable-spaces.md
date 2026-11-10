---
declaration: theorem
origin: cited
lean: WeaklyFirstCountable.exists_weakly_first_countable_not_first_countable, WeaklyFirstCountable.existsWeaklyFirstCountableCompactBig, WeaklyFirstCountable.existsWeaklyFirstCountableCompactNotFirstCountable, WeaklyFirstCountable.CH.existsWeaklyFirstCountableCompactNotFirstCountable, WeaklyFirstCountable.cardinalMk_le_continuum_of_weaklyFirstCountable_of_countableSouslinNumber
statement: formalized
---

# Conjectures about Weakly First Countable spaces

> This file formalizes the notion of a weakly first countable topological space and some conjectures
> around those.
>
> *References:*
> * [Ar2013] Arhangeliski, Alexandr. "Selected old open problems in general topology."
>   Buletinul Academiei de Ştiinţe a Republicii Moldova. Matematica 73.2-3 (2013): 37-46.
>   https://www.math.md/files/basm/y2013-n2-3/y2013-n2-3-(pp37-46).pdf.pdf
> * [Ya1976] Yakovlev, N. N. "On the theory of o-metrizable spaces."
>   Doklady Akademii Nauk. Vol. 229. No. 6. Russian Academy of Sciences, 1976.
>   https://www.mathnet.ru/links/016f74007f9f96fa3aadae05cbd98457/dan40570.pdf (in Russian)

*Quoted from [FormalConjectures/Paper/WeaklyFirstCountable.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/WeaklyFirstCountable.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 3 open, 1 solved and 1 textbook result. It also has 2 test statements, counted here but not shown.

## `WeaklyFirstCountable.exists_weakly_first_countable_not_first_countable`

Textbook result, stated without proof.

> There are weakly first countable spaces which are not first countable,
> for example the [Arens Space](https://topology.pi-base.org/spaces/S000156).

```lean
theorem exists_weakly_first_countable_not_first_countable : ∃ (X : Type) (_ : TopologicalSpace X),
      WeaklyFirstCountableTopology X ∧ ¬ FirstCountableTopology X
```

Category `textbook`; AMS [54 General topology](../../by-subject/part-02/54-general-topology/README.md). Declared in [FormalConjectures/Paper/WeaklyFirstCountable.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/WeaklyFirstCountable.lean#L73).

## `WeaklyFirstCountable.existsWeaklyFirstCountableCompactBig`

Open: stated without proof.

> Problem 2 in [Ar2013]: Give an example in ZFC of a weakly first-
> countable compact Hausdorff space X such that $𝔠 < |X|$.
>
> Note: [Ar2013] uses a blanket convention that all spaces are
> Tychonoff and "compact" means compact Hausdorff.

```lean
theorem existsWeaklyFirstCountableCompactBig :
    ∃ (X : Type) (_ : TopologicalSpace X),
      WeaklyFirstCountableTopology X ∧ CompactSpace X ∧ T2Space X ∧
        𝔠 < #X
```

Category `research open`; AMS [54 General topology](../../by-subject/part-02/54-general-topology/README.md). Declared in [FormalConjectures/Paper/WeaklyFirstCountable.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/WeaklyFirstCountable.lean#L114).

## `WeaklyFirstCountable.existsWeaklyFirstCountableCompactNotFirstCountable`

Open: stated without proof.

> Problem 3 in [Ar2013]: Give an example in ZFC of a weakly first-
> countable compact Hausdorff space which is not first countable.
>
> Note: [Ar2013] uses a blanket convention that all spaces are
> Tychonoff and "compact" means compact Hausdorff.

```lean
theorem existsWeaklyFirstCountableCompactNotFirstCountable :
    ∃ (X : Type) (_ : TopologicalSpace X),
      WeaklyFirstCountableTopology X ∧ CompactSpace X ∧ T2Space X ∧
        ¬ FirstCountableTopology X
```

Category `research open`; AMS [54 General topology](../../by-subject/part-02/54-general-topology/README.md). Declared in [FormalConjectures/Paper/WeaklyFirstCountable.lean, line 126](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/WeaklyFirstCountable.lean#L126).

## `WeaklyFirstCountable.CH.existsWeaklyFirstCountableCompactNotFirstCountable`

Solved: stated here without proof.

> Under CH, such a space (for Problem 3 in [Ar2013]) exists as
> constructed in [Ya1976] by Yakovlev.

```lean
theorem CH.existsWeaklyFirstCountableCompactNotFirstCountable
    [Fact (ℵ₁ = 𝔠)] :
    ∃ (X : Type) (_ : TopologicalSpace X),
      WeaklyFirstCountableTopology X ∧ CompactSpace X ∧ T2Space X ∧
        ¬ FirstCountableTopology X
```

Category `research solved`; AMS [54 General topology](../../by-subject/part-02/54-general-topology/README.md). Declared in [FormalConjectures/Paper/WeaklyFirstCountable.lean, line 135](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/WeaklyFirstCountable.lean#L135).

## `WeaklyFirstCountable.cardinalMk_le_continuum_of_weaklyFirstCountable_of_countableSouslinNumber`

Open: stated without proof.

> Problem 4 in [Ar2013]: If a Tychonoff weakly first-countable space has countable
> Souslin number, then does its cardinality not exceed the continuum?

```lean
theorem cardinalMk_le_continuum_of_weaklyFirstCountable_of_countableSouslinNumber :
    ∀ (X : Type) (_ : TopologicalSpace X), T35Space X →
      WeaklyFirstCountableTopology X → HasCountableSouslinNumber X → #X ≤ 𝔠
```

Category `research open`; AMS [54 General topology](../../by-subject/part-02/54-general-topology/README.md). Declared in [FormalConjectures/Paper/WeaklyFirstCountable.lean, line 144](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/WeaklyFirstCountable.lean#L144).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/WeaklyFirstCountable.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/WeaklyFirstCountable.lean)
- [https://www.math.md/files/basm/y2013-n2-3/y2013-n2-3-(pp37-46](https://www.math.md/files/basm/y2013-n2-3/y2013-n2-3-%28pp37-46)
