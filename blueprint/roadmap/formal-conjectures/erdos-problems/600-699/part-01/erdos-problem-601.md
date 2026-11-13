---
declaration: theorem
origin: cited
lean: Erdos601.erdos_601, Erdos601.erdos_601.variants.universal, Erdos601.erdos_601.variants.erdos_hajnal_milner_1970, Erdos601.erdos_601.variants.omega_1_omega_plus_2, Erdos601.erdos_601.variants.at_omega
statement: formalized
---

# Erdős Problem 601

> *Reference:* [erdosproblems.com/601](https://www.erdosproblems.com/601)
>
> *References:*
> - [EHM70] Erdős, P.; Hajnal, A.; Milner, E.C. *Set mappings and polarized partition relations.*
>   Combinatorial theory and its applications, I–III (Balatonfüred, 1969) (1970), 327–363.
> - [Er81] Erdős, P. *On the combinatorial problems which I would most like to see solved.*
>   Combinatorica 1 (1981), 25–42, Section VII.
> - [La90] Larson, J.A. *Martin's Axiom and ordinal graphs: large independent sets or infinite
>   paths.* Ann. Pure Appl. Logic 47 (1990), 31–39.

*Quoted from [FormalConjectures/ErdosProblems/601.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/601.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/601](https://www.erdosproblems.com/601).

The file states 5 research or textbook statements: 3 open and 2 solved.

## `Erdos601.erdos_601`

Open: stated without proof.

> **Erdős Problem 601** ($500 prize).
>
> For which limit ordinals $\alpha$ does `HasPathOrIndepSetOfType α` hold?

```lean
theorem erdos_601 :
    ∀ α : Ordinal.{0}, Order.IsSuccLimit α →
      (HasPathOrIndepSetOfType α ↔
        erdos_601.answer α)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/601.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/601.lean#L66).

## `Erdos601.erdos_601.variants.universal`

Open: stated without proof.

> **Erdős–Hajnal–Milner conjecture** [Er81, Section VII]: every graph on a limit ordinal
> $\alpha$ contains an infinite path or an independent set of order type $\alpha$.

```lean
theorem erdos_601.variants.universal :
    ∀ α : Ordinal.{0}, Order.IsSuccLimit α → HasPathOrIndepSetOfType α
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/601.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/601.lean#L76).

## `Erdos601.erdos_601.variants.erdos_hajnal_milner_1970`

Solved: stated here without proof.

> **Erdős–Hajnal–Milner (1970)** [EHM70]: For all limit ordinals $\alpha < \omega_1^{\omega+2}$,
> every graph on $\alpha.\mathrm{ToType}$ has either an infinite path or an independent set of
> order type $\alpha$.

```lean
theorem erdos_hajnal_milner_1970 :
    ∀ α : Ordinal.{0},
      Order.IsSuccLimit α →
      α < ω_ 1 ^ (ω + 2) →
      HasPathOrIndepSetOfType α
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/601.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/601.lean#L88).

## `Erdos601.erdos_601.variants.omega_1_omega_plus_2`

Open: stated without proof.

> **Erdős–Hajnal–Milner conjecture at $\omega_1^{\omega+2}$** [Er81, Section VII]: every
> graph on $\omega_1^{\omega+2}$ contains an infinite path or an independent set of that
> order type. Erdős conjectured the positive answer. This is the first limit ordinal not
> covered by the Erdős–Hajnal–Milner theorem.

```lean
theorem omega_1_omega_plus_2 :
    HasPathOrIndepSetOfType (ω_ 1 ^ (ω + 2))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/601.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/601.lean#L102).

## `Erdos601.erdos_601.variants.at_omega`

Solved: stated here without proof.

> **Base case $\alpha = \omega$**: `HasPathOrIndepSetOfType ω` holds.
>
> Every countably infinite graph on vertex set $\omega$ either contains an infinite path or
> has an infinite independent set (and an infinite set has order type $\omega$). Follows from
> Ramsey-theoretic arguments (or directly from the Erdős–Hajnal–Milner result since
> $\omega < \omega_1^{\omega+2}$).

```lean
theorem at_omega : HasPathOrIndepSetOfType ω
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/601.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/601.lean#L122).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/601.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/601.lean)
- [erdosproblems.com/601](https://www.erdosproblems.com/601)
