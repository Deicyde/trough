---
declaration: theorem
origin: cited
lean: Erdos596.erdos_596, Erdos596.erdos_596.variants.exists_exceptional, Erdos596.erdos_596.variants.C4_free_countable_escape, Erdos596.erdos_596.variants.C4_C6_finite_ramsey, Erdos596.erdos_596.variants.C4_C6_is_exceptional, Erdos596.erdos_596.variants.original_conjecture_is_false, Erdos596.erdos_596.variants.K4_K3_exceptional_iff, Erdos596.erdos_596.variants.K4_K3_finite_ramsey
statement: formalized
---

# Erdős Problem 596

> *References:*
> - [erdosproblems.com/596](https://www.erdosproblems.com/596)
> - [Er87] Erdős, *Some of my favourite problems in various branches of combinatorics*,
>   *Mat. Lapok* 1987.
> - [NeRo75] Nešetřil and Rödl, *The Ramsey property for graphs with forbidden complete
>   subgraphs*, *J. Combin. Theory* B **20** (1976), 243--249.

*Quoted from [FormalConjectures/ErdosProblems/596.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/596.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/596](https://www.erdosproblems.com/596).

The file states 8 research or textbook statements: 2 open and 6 solved. It also has 1 test statement, counted here but not shown.

## `Erdos596.erdos_596`

Open: stated without proof.

> **Erdős Problem 596** (Erdős–Hajnal, [Er87]). For which graph pairs $(G_1, G_2)$ is it
> true that
>
>   (1) for every $n \geq 1$ there is a graph $H$ without a $G_1$ such that any
>       $n$-colouring of $H$'s edges contains a monochromatic $G_2$, and yet
>   (2) for every graph $H$ without a $G_1$ there is an $\aleph_0$-colouring of $H$'s edges
>       with no monochromatic $G_2$?
>
> Erdős and Hajnal originally conjectured that no such pair exists; but $(C_4, C_6)$
> witnesses it (Nešetřil–Rödl + Erdős–Hajnal). The full question is to characterise the
> class of all such pairs, recorded here as the unknown `erdos_596.answer`.
>
> See Problem 595 for the specific case $(G_1, G_2) = (K_4, K_3)$.

```lean
theorem erdos_596 :
    ∀ {U₁ U₂ : Type} (G₁ : SimpleGraph U₁) (G₂ : SimpleGraph U₂),
      IsErdosHajnalExceptional G₁ G₂ ↔ erdos_596.answer G₁ G₂
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/596.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/596.lean#L55).

## `Erdos596.erdos_596.variants.exists_exceptional`

Solved: stated here without proof.

> Erdős–Hajnal exceptional pairs exist — recorded as a known direction of `erdos_596`.

```lean
theorem erdos_596.variants.exists_exceptional :
    ∃ (U₁ U₂ : Type) (G₁ : SimpleGraph U₁) (G₂ : SimpleGraph U₂),
      IsErdosHajnalExceptional G₁ G₂
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/596.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/596.lean#L62).

## `Erdos596.erdos_596.variants.C4_free_countable_escape`

Solved: stated here without proof.

> Every $C_4$-free graph is a countable union of trees (Erdős–Hajnal [Er87]); trees are
> acyclic, hence $C_6$-free, giving the countable Ramsey escape for $(C_4, C_6)$.

```lean
theorem erdos_596.variants.C4_free_countable_escape :
    HasCountableRamseyEscape (cycleGraph 4) (cycleGraph 6)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/596.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/596.lean#L70).

## `Erdos596.erdos_596.variants.C4_C6_finite_ramsey`

Solved: stated here without proof.

> Nešetřil–Rödl [NeRo75]: for every $n \geq 1$ there is a $C_4$-free graph whose edges
> cannot be $n$-coloured without a monochromatic $C_6$.

```lean
theorem erdos_596.variants.C4_C6_finite_ramsey :
    HasFiniteRamseyProperty (cycleGraph 4) (cycleGraph 6)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/596.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/596.lean#L77).

## `Erdos596.erdos_596.variants.C4_C6_is_exceptional`

Proved here.

> The pair $(C_4, C_6)$ is Erdős–Hajnal exceptional; combines `C4_C6_finite_ramsey` and
> `C4_free_countable_escape`.

```lean
theorem erdos_596.variants.C4_C6_is_exceptional :
    IsErdosHajnalExceptional (cycleGraph 4) (cycleGraph 6)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/596.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/596.lean#L84).

## `Erdos596.erdos_596.variants.original_conjecture_is_false`

Solved: stated here without proof.

> The original Erdős–Hajnal conjecture (that no exceptional pair exists) is **false** —
> witnessed by $(C_4, C_6)$ via `C4_C6_is_exceptional`.

```lean
theorem erdos_596.variants.original_conjecture_is_false :
    ¬ ∀ {U₁ U₂ : Type} (G₁ : SimpleGraph U₁) (G₂ : SimpleGraph U₂),
      ¬IsErdosHajnalExceptional G₁ G₂
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/596.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/596.lean#L91).

## `Erdos596.erdos_596.variants.K4_K3_exceptional_iff`

Open: stated without proof.

> Whether $(K_4, K_3)$ is Erdős–Hajnal exceptional is precisely the content of
> Erdős Problem 595. The finite Ramsey property holds (Folkman 1970, Nešetřil–Rödl
> [NeRo75]); the open part is whether every $K_4$-free graph is a countable union of
> triangle-free graphs.

```lean
theorem erdos_596.variants.K4_K3_exceptional_iff :
    IsErdosHajnalExceptional (completeGraph (Fin 4)) (completeGraph (Fin 3))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/596.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/596.lean#L101).

## `Erdos596.erdos_596.variants.K4_K3_finite_ramsey`

Solved: stated here without proof.

> Folkman 1970 / Nešetřil–Rödl [NeRo75]: for every $n \geq 1$ there is a $K_4$-free
> graph whose edges cannot be $n$-coloured without a monochromatic triangle.

```lean
theorem erdos_596.variants.K4_K3_finite_ramsey :
    HasFiniteRamseyProperty (completeGraph (Fin 4)) (completeGraph (Fin 3))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/596.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/596.lean#L108).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/596.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/596.lean)
- [erdosproblems.com/596](https://www.erdosproblems.com/596)
