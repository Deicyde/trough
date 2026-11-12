---
declaration: section
origin: cited
lean: OAI.TwoWayComplementation.complementation_lower_bound_finite, OAI.TwoWayComplementation.explicit_family_main, OAI.OneWayLiveness.main_theorem
statement: formalized
proof: formalized
---

# 129. Exponential state costs for two-way automata

2 manuscripts and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves exponential lower bounds both for complementing two-way nondeterministic finite automata and for simulating one-way nondeterministic automata by two-way deterministic ones. The latter resolves the Sakoda–Sipser state-succinctness conjecture over growing finite alphabets; both results rule out polynomial state bounds independent of alphabet size.

## An exponential state lower bound for two-way nondeterministic complementation

We prove that two-way nondeterministic finite automata cannot be complemented with a polynomial number of states independent of the alphabet. For each *n* ≥ 4 we construct an *n*-state automaton over a finite alphabet whose complement requires at least $\tfrac12 2^{\lfloor(n-4)/127\rfloor}-1$ states.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-exponential-state-lower-bound-for-two-way-nondeterministic-complementation-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## An exponential two-way deterministic state lower bound for one-way liveness

One-way liveness on *h* points accepts a word of binary relations when their ordered product is nonempty. For every *h* ≥ 2, it has a nondeterministic automaton with $h+3$ states and no left moves, whereas every equivalent *s*-state two-way deterministic automaton satisfies $4(s+2)^2\ge2^{\lfloor(h-2)/31\rfloor}$. Partial transition rules, stay moves, and nonaccepting infinite computations are allowed. The alphabets are finite and grow with *h*, so the result rules out an alphabet-independent polynomial state bound for deterministic two-way simulation, already for one-way nondeterministic sources.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-exponential-two-way-deterministic-state-lower-bound-for-one-way-liveness-September-25-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The paper asks how many states are needed to complement or determinize two-way nondeterministic finite automata. The formalization gives, for every $n\ge4$, an explicit $n$-state automaton whose complement requires at least $\tfrac12 2^{\lfloor(n-4)/127\rfloor}-1$ states. For the same family of relational languages and every $n\ge131$, every equivalent deterministic two-way automaton requires at least $\tfrac12 2^{\lfloor(n-4)/127\rfloor}$ states.

The alphabet grows with $n$, so neither complementation nor determinization has a polynomial state bound uniform over alphabets. The model has two endmarkers, left, right, and stay moves, and acceptance by a finite run. The separate results about one-way liveness and the Sakoda–Sipser problem are outside this scope.

The formalization gives a family of one-way nondeterministic automata with $h+3$ states whose languages require exponentially many states for two-way deterministic recognition. For every $h\ge2$, a deterministic recognizer with $s$ states satisfies $2^{\lfloor(h-2)/31\rfloor}\le4(s+2)^2$ under both acceptance conventions considered in the paper; one convention has the sharper factor $4(s+1)^2$. The alphabet may grow with $h$, so no alphabet-independent polynomial simulation bound holds.

## Lean: Two-way nondeterministic complementation lower bound

Stated in [TwoWayComplementation.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TwoWayComplementation.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem complementation_lower_bound_finite (n : ℕ) (hn : 4 ≤ n) :
    ∃ A : TwoNFA (SetRel (Fin (n - 2)) (Fin (n - 2))) (Fin n),
      ∀ (Q : Type*) [Fintype Q], ∀ B : TwoNFA (SetRel (Fin (n - 2)) (Fin (n - 2))) Q,
        B.language = A.languageᶜ →
          (1 / 2 : ℝ) * 2 ^ ((n - 4) / 127) - 1 ≤ (Fintype.card Q : ℝ)
```

Proved in [lean/OAI/Combinatorics/TwoWayAutomata/Main.lean, line 31](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/TwoWayAutomata/Main.lean#L31).

## Lean: Same-family determinization lower bound

Stated in [TwoWayDeterminization.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TwoWayDeterminization.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem explicit_family_main (n : ℕ) (hn : 4 ≤ n) :
    ∃ A : TwoNFA (SetRel (Fin (n - 2)) (Fin (n - 2))) (Fin n),
      A.language = sourceLanguage (Fin (n - 2)) ∧
      (∀ (Q : Type*) [Fintype Q],
        ∀ B : TwoNFA (SetRel (Fin (n - 2)) (Fin (n - 2))) Q,
        B.language = A.languageᶜ →
          (1 / 2 : ℝ) * 2 ^ ((n - 4) / 127) - 1 ≤ (Fintype.card Q : ℝ)) ∧
      (131 ≤ n → ∀ (Q : Type*) [Fintype Q],
        ∀ D : TwoNFA (SetRel (Fin (n - 2)) (Fin (n - 2))) Q,
        D.Deterministic → D.language = A.language →
          (1 / 2 : ℝ) * 2 ^ ((n - 4) / 127) ≤ (Fintype.card Q : ℝ))
```

Proved in [lean/OAI/Combinatorics/TwoWayAutomata/ExplicitFamily.lean, line 36](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/TwoWayAutomata/ExplicitFamily.lean#L36).

## Lean: Exponential deterministic state lower bound for liveness

Stated in [OneWayLiveness.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/OneWayLiveness.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main_theorem (h : ℕ) (hh : 2 ≤ h) :
    (∃ N : NMachine (Alphabet h) (h + 3), N.NoLeft ∧
      ∀ positive : Bool, N.Recognizes positive (OWL h)) ∧
    (∀ (positive : Bool) (s : ℕ) (D : DMachine (Alphabet h) s),
      D.Recognizes positive (OWL h) →
      2 ^ ((h - 2) / 31) ≤ 4 * (s + if positive then 2 else 1) ^ 2)
```

Proved in [lean/OAI/Combinatorics/Automata/Main.lean, line 10](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/Automata/Main.lean#L10).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/129.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/129.md)
