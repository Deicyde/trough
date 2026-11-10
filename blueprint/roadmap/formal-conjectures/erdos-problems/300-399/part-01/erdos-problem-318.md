---
declaration: theorem
origin: cited
lean: Erdos318.erdos_318.variants.univ, Erdos318.erdos_318.variants.odd, Erdos318.erdos_318.variants.contain_single_even, Erdos318.erdos_318.parts.i, Erdos318.erdos_318.variants.infinite_AP, Erdos318.erdos_318.parts.ii
statement: formalized
---

# Erdős Problem 318

> *References:*
>   - [erdosproblems.com/318](https://www.erdosproblems.com/318)
>   - [ErSt75] Erdős, P. and Straus, E. G., Solution to Problem 387. Nieuw Arch. Wisk. (1975), 183.
>   - [Sa75] Sattler, R., Solution to Problem 387. Nieuw Arch. Wisk. (1975), 184-189.
>   - [Sa82b] Sattler, R., On Erdős property P₁ for the arithmetical sequence. Nederl. Akad. Wetensch.
>     Indag. Math. (1982), 347--352.
>   - [ErGr80] Erdős, P. and Graham, R., Old and new problems and results in combinatorial number
>     theory. Monographies de L'Enseignement Mathematique (1980).
>   - [La26] D. Larsen, [Erdős problem 318](https://github.com/Larsen-Daniel/Erdos-318/blob/main/318.pdf) (2026)

*Quoted from [FormalConjectures/ErdosProblems/318.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/318.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/318](https://www.erdosproblems.com/318).

The file states 6 research or textbook statements: 6 solved. It also has 1 test statement, counted here but not shown.

## `Erdos318.erdos_318.variants.univ`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos318.lean#L761](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos318.lean#L761).

> `ℕ` has property `P₁`. This is proved in [ErSt75].

```lean
theorem erdos_318.variants.univ : P₁ univ
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/318.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/318.lean#L53).

## `Erdos318.erdos_318.variants.odd`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos318.lean#L782](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos318.lean#L782).

> Sattler proved in [Sa75] that the set of odd numbers has property `P₁`.

```lean
theorem erdos_318.variants.odd : P₁ {n | Odd n}
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/318.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/318.lean#L60).

## `Erdos318.erdos_318.variants.contain_single_even`

Solved: stated here without proof.

> For any infinite set `A` containing exactly one positive even number, `A` does not have
> property `P₁`. Sattler [Sa82] credits this observation to Erdős, who presumably found this after
> [ErGr80]. The element `0` is not counted, since `P₁` ignores it, and the infinitude hypothesis
> excludes degenerate sets such as `{2}`, on which `P₁` holds vacuously.

```lean
theorem erdos_318.variants.contain_single_even {A : Set ℕ} (hA : A.Infinite)
    (hA' : {n | n ∈ A \ {0} ∧ Even n}.ncard = 1) : ¬ P₁ A
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/318.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/318.lean#L114).

## `Erdos318.erdos_318.parts.i`

Solved: stated here without proof.

> There exists a set `A` with positive density that does not have property `P₁`.
> #TODO: prove this lemma by assuming `erdos_318.contain_single_even`.
>
> The density sits in an existential, so `HasPosDensity` is the *stronger* reading here and
> weakening it to positive lower density would claim less, which is the opposite of the usual
> situation for Erdős' "positive density". It also costs nothing: by
> `erdos_318.variants.contain_single_even` a witness only needs exactly one even element, and the
> odd numbers together with one even number have density `1 / 2` on the nose.

```lean
theorem erdos_318.parts.i : ∃ A : Set ℕ, HasPosDensity A ∧ ¬ P₁ A
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/318.lean, line 127](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/318.lean#L127).

## `Erdos318.erdos_318.variants.infinite_AP`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos318.lean#L599](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos318.lean#L599).

> Every infinite arithmetic progression has property `P₁`. This is proved in [Sa82b].

```lean
theorem erdos_318.variants.infinite_AP {A : Set ℕ} (hA : A.IsAPOfLength ⊤) : P₁ A
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/318.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/318.lean#L134).

## `Erdos318.erdos_318.parts.ii`

Solved: stated here without proof.

> Does the set of squares excluding 1 have property `P₁`?
>
> Larsen [La26] proved that this set does have property `P₁`.

```lean
theorem erdos_318.parts.ii : P₁ ({n | IsSquare n} \ {1})
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/318.lean, line 143](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/318.lean#L143).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/318.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/318.lean)
- [erdosproblems.com/318](https://www.erdosproblems.com/318)
