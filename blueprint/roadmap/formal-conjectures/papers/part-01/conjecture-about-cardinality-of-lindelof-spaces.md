---
declaration: theorem
origin: cited
lean: CardinalityLindelof.HasGδSingletons.lindelof_card
statement: formalized
---

# Conjecture about cardinality of Lindelöf spaces

> The conjecture asks for a Lindelöf Tychonoff space where all singletons are G_δ sets
> and which has cardinality > 𝔠.
>
> This is Problem 1 in https://www.math.md/files/basm/y2013-n2-3/y2013-n2-3-(pp37-46).pdf.pdf
>
> *Reference:*
> * [Selected Old Open Problems in General Topology](https://www.math.md/files/basm/y2013-n2-3/y2013-n2-3-(pp37-46).pdf.pdf)
>   by A. V. Arhangel’skii

*Quoted from [FormalConjectures/Paper/CardinalityLindelof.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/CardinalityLindelof.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `CardinalityLindelof.HasGδSingletons.lindelof_card`

Open: stated without proof.

> Is there a Lindelöf Tychonoff space with singletons as Gδ sets with cardinality greater than
> the continuum?
>
> Note: the cited paper uses a blanket convention that all spaces are Tychonoff.

```lean
theorem HasGδSingletons.lindelof_card :
    ∃ (X : Type) (_ : TopologicalSpace X),
      T35Space X ∧ HasGδSingletons X ∧ LindelofSpace X ∧ 𝔠 < #X
```

Category `research open`; AMS [54 General topology](../../by-subject/part-02/54-general-topology/README.md). Declared in [FormalConjectures/Paper/CardinalityLindelof.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/CardinalityLindelof.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/CardinalityLindelof.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/CardinalityLindelof.lean)
- [Selected Old Open Problems in General Topology](https://www.math.md/files/basm/y2013-n2-3/y2013-n2-3-%28pp37-46%29.pdf.pdf)
