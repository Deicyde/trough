---
declaration: section
origin: cited
lean: OAI.LinearListHadwiger.main_theorem, OAI.HadwigerCounterexample.exists_counterexamples, OAI.HadwigerCounterexample.not_hadwiger_conjecture
statement: formalized
proof: formalized
---

# 157. Graph coloring, clique minors, and Colin de Verdière invariants

3 manuscripts and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Disproves Hadwiger's conjecture even for fractional coloring: arbitrarily large finite simple graphs with independence number at most two satisfy $\chi_f(G)\gt h(G)$, where $h(G)$ is the largest clique-minor order. Also disproves the fractional Colin de Verdière chromatic bound $\chi_f(G)\le\mu(G)+1$. In the positive direction, every finite nonempty graph satisfies $\chi_{\mathrm{list}}(G)\le C h(G)$ for a universal constant *C*.

## A counterexample to Hadwiger's conjecture

We disprove Hadwiger's conjecture by constructing arbitrarily large graphs whose chromatic number exceeds their Hadwiger number. The examples have independence number at most two, and even their ordinary fractional chromatic number exceeds their Hadwiger number. Thus they also disprove the fractional-coloring weakening discussed by Reed and Seymour.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## A counterexample to the Colin de Verdière chromatic conjecture

We disprove the Colin de Verdière chromatic conjecture by constructing graphs whose chromatic number exceeds their Colin de Verdière invariant by more than one. The examples have independence number at most two. In fact, their ordinary fractional chromatic number also exceeds their Colin de Verdière invariant by more than one.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-counterexample-to-the-Colin-de-Verdiere-chromatic-conjecture-September-23-2026/paper.pdf).

## A linear list-coloring bound in terms of the Hadwiger number

We prove that every finite nonempty graph *G* satisfies $\chi_{\mathrm{list}}(G)\le C h(G)$ for an absolute integer *C*, where $h(G)$ is the largest order of a clique minor. This resolves the Linear List Hadwiger conjecture affirmatively.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Hadwiger's conjecture predicts $\chi(G)\le h(G)$ for every finite graph, where $h(G)$ is the largest clique-minor order. The formalization constructs arbitrarily large finite simple counterexamples with independence number at most two. For a graph on $m$ vertices it proves
$h(G)<26m/75+2/3<m/2\le\chi(G)$.
This disproves the ordinary chromatic form. The paper's fractional-chromatic strengthening and the Colin de Verdière consequence are outside this selected statement.

The Linear List Hadwiger conjecture asks for a universal linear bound on list chromatic number in terms of clique-minor size. The formalization proves that there is one integer $C\ge1$ such that every finite nonempty simple graph $G$ satisfies $\chi_{\mathrm{list}}(G)\le C h(G)$, where $h(G)$ is the largest order of a clique minor. The constant is independent of the graph.

## Lean: Linear list-coloring bound in the Hadwiger number

Stated in [ListHadwiger.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ListHadwiger.lean).

```lean
theorem main_theorem : MainStatement
```

Proved in [lean/OAI/Combinatorics/ListHadwiger/Main.lean, line 58](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/ListHadwiger/Main.lean#L58).

## Lean: Arbitrarily large counterexamples to Hadwiger's conjecture

Stated in [HadwigerCounterexample.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HadwigerCounterexample.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem exists_counterexamples (M : ℕ) : ∃ m : ℕ, max M 5 ≤ m ∧
    ∃ G : SimpleGraph (Fin m), G.indepNum ≤ 2 ∧
      (connectedMatchingNumber G : ℚ) < (m : ℚ) / 100 ∧
      (hadwigerNumber G : ℚ) < 26 * (m : ℚ) / 75 + 2 / 3 ∧
      26 * (m : ℚ) / 75 + 2 / 3 < (m : ℚ) / 2 ∧
      (m : ℚ) / 2 ≤ (G.chromaticNumber.toNat : ℚ) ∧
      hadwigerNumber G < G.chromaticNumber.toNat ∧
      G.chromaticNumber ≠ ⊤ ∧
      G.chromaticNumber = ↑(G.chromaticNumber.toNat)
```

Proved in [lean/OAI/Combinatorics/HadwigerCounterexample/Main.lean, line 101](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/HadwigerCounterexample/Main.lean#L101).

```lean
theorem not_hadwiger_conjecture :
    ¬ (∀ (m : ℕ) (G : SimpleGraph (Fin m)),
      G.chromaticNumber ≤ ↑(hadwigerNumber G))
```

Proved in [lean/OAI/Combinatorics/HadwigerCounterexample/Main.lean, line 120](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/HadwigerCounterexample/Main.lean#L120).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/157.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/157.md)
