---
declaration: theorem
origin: cited
lean: EquationalTheories_677_255.Equation255_not_implies_Equation677, EquationalTheories_677_255.Equation677_not_implies_Equation255, EquationalTheories_677_255.Finite.Equation255_not_implies_Equation677, EquationalTheories_677_255.Finite.Equation677_implies_Equation255
statement: formalized
---

# Equational Theories

> *Reference:* [Equational Theories project site](https://teorth.github.io/equational_theories/implications/?677&finite)

*Quoted from [FormalConjectures/Other/EquationalTheories_677_255.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Other/EquationalTheories_677_255.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 1 open and 3 solved.

## `EquationalTheories_677_255.Equation255_not_implies_Equation677`

Proved here.

> Equation 255 does not imply Equation 677.

```lean
theorem Equation255_not_implies_Equation677 :
    ∃ (G : Type) (_ : Magma G), Equation255 G ∧ ¬ Equation677 G
```

Category `research solved`; AMS [08 General algebraic systems](../by-subject/part-01/08-general-algebraic-systems/README.md). Declared in [FormalConjectures/Other/EquationalTheories_677_255.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Other/EquationalTheories_677_255.lean#L41).

## `EquationalTheories_677_255.Equation677_not_implies_Equation255`

Solved: stated here without proof.

> Equation 677 does not imply Equation 255.

```lean
theorem Equation677_not_implies_Equation255 :
    ∃ (G : Type) (_ : Magma G), Equation677 G ∧ ¬ Equation255 G
```

Category `research solved`; AMS [08 General algebraic systems](../by-subject/part-01/08-general-algebraic-systems/README.md). Declared in [FormalConjectures/Other/EquationalTheories_677_255.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Other/EquationalTheories_677_255.lean#L48).

## `EquationalTheories_677_255.Finite.Equation255_not_implies_Equation677`

Proved here.

> Note that this is a stronger form of `Equation255_not_implies_Equation677`.

```lean
theorem Finite.Equation255_not_implies_Equation677 :
    ∃ (G : Type) (_ : Magma G), Finite G ∧ Equation255 G ∧ ¬ Equation677 G
```

Category `research solved`; AMS [08 General algebraic systems](../by-subject/part-01/08-general-algebraic-systems/README.md). Declared in [FormalConjectures/Other/EquationalTheories_677_255.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Other/EquationalTheories_677_255.lean#L54).

## `EquationalTheories_677_255.Finite.Equation677_implies_Equation255`

Open: stated without proof.

> **Equational Theories, Problem 8.1.** Does Equation 677 imply Equation 255 in every finite
> magma? The project tentatively conjectures that the answer is no; a false answer is equivalent to
> the existence of a finite countermodel satisfying Equation 677 but not Equation 255.
>
>
> Discussion thread:
> https://leanprover.zulipchat.com/#narrow/channel/458659-Equational/topic/FINITE.3A.20677.20-.3E.20255

```lean
theorem Finite.Equation677_implies_Equation255 :
    ∀ (G : Type) (_ : Magma G), Finite G → Equation677 G → Equation255 G
```

Category `research open`; AMS [08 General algebraic systems](../by-subject/part-01/08-general-algebraic-systems/README.md). Declared in [FormalConjectures/Other/EquationalTheories_677_255.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Other/EquationalTheories_677_255.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Other/EquationalTheories_677_255.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Other/EquationalTheories_677_255.lean)
- [Equational Theories project site](https://teorth.github.io/equational_theories/implications/?677&finite)
