---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.MarkovDecision.improve, Cslib.Algorithms.Lean.MarkovDecision.policyIteration, Cslib.Algorithms.Lean.MarkovDecision.le_policyValue_of_le_policyBellman, Cslib.Algorithms.Lean.MarkovDecision.policyValue_le_policyValue_improve, Cslib.Algorithms.Lean.MarkovDecision.policyValue_improve_eq_iff, Cslib.Algorithms.Lean.MarkovDecision.policyValue_improve_ne, Cslib.Algorithms.Lean.MarkovDecision.policyValue_policyIteration_mono, Cslib.Algorithms.Lean.MarkovDecision.policyValue_policyIteration_of_eq
statement: formalized
proof: formalized
---

# Policy iteration

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/policy-iteration/index.html).

## Policy improvement step

Let $M$ be a Markov decision process with a finite set of states
$S$, a finite nonempty set of actions $A$, real rewards $r(s, a)$ and stochastic transition
probabilities $P(s' \mid s, a)$, and let $0 \le \gamma < 1$. The improvement of a deterministic
policy $\pi : S \to A$ is a fixed choice of policy greedy for the value $V^\pi$ of $\pi$: in each
state $s$ it takes a chosen action $a$ maximizing
$r(s, a) + \gamma \sum_{s'} P(s' \mid s, a) V^\pi(s')$ over $A$ (ties broken arbitrarily).

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.improve`, a definition declared in [CSLibExt/Algorithms/Lean/MDP/PolicyIteration.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/PolicyIteration.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/policy-iteration/index.html#improve).

## Policy iteration

Let $M$ be a Markov decision process with a finite set of states $S$, a
finite nonempty set of actions $A$, real rewards and stochastic transition probabilities, and let
$0 \le \gamma < 1$. Policy iteration run for $n$ steps from a deterministic policy $\pi : S \to A$
is the policy obtained from $\pi$ by applying the policy improvement step $n$ times.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.policyIteration`, a definition declared in [CSLibExt/Algorithms/Lean/MDP/PolicyIteration.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/PolicyIteration.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/policy-iteration/index.html#policy-iteration).

## Values below their Bellman image lie below the policy value

Let $M$ be a Markov decision
process with a finite set of states $S$, real rewards and stochastic transition probabilities,
and let $0 \le \gamma < 1$. Let $\pi$ be a deterministic policy, with Bellman operator $T^\pi$ and
value $V^\pi$. If $V : S \to \mathbb{R}$ satisfies $V(s) \le (T^\pi V)(s)$ for every state $s$,
then $V(s) \le V^\pi(s)$ for every state $s$.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.le_policyValue_of_le_policyBellman`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/PolicyIteration.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/PolicyIteration.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/policy-iteration/index.html#le-policy-value-of-le-policy-bellman).

## Policy improvement theorem

Let $M$ be a Markov decision process with a finite set of
states $S$, a finite nonempty set of actions $A$, real rewards and stochastic transition
probabilities, and let $0 \le \gamma < 1$. Write $V^\pi$ for the value of a deterministic policy
$\pi : S \to A$. For every deterministic policy $\pi$, the improved policy $\pi'$, which is greedy
for $V^\pi$, satisfies $V^\pi(s) \le V^{\pi'}(s)$ for every state $s$.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.policyValue_le_policyValue_improve`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/PolicyIteration.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/PolicyIteration.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/policy-iteration/index.html#policy-value-le-policy-value-improve).

## Improvement stalls exactly at optimal policies

Let $M$ be a Markov decision process with a
finite set of states $S$, a finite nonempty set of actions $A$, real rewards and stochastic
transition probabilities, and let $0 \le \gamma < 1$. Write $V^\pi$ for the value of a
deterministic policy $\pi : S \to A$ and $V^*$ for the optimal value. For every deterministic
policy $\pi$, with improved policy $\pi'$, we have $V^{\pi'} = V^\pi$ if and only if
$V^\pi = V^*$ (as functions on $S$).

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.policyValue_improve_eq_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/PolicyIteration.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/PolicyIteration.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/policy-iteration/index.html#policy-value-improve-eq-iff).

## Away from optimality, improvement changes the value

Let $M$ be a Markov decision process
with a finite set of states $S$, a finite nonempty set of actions $A$, real rewards and stochastic
transition probabilities, and let $0 \le \gamma < 1$. Write $V^\pi$ for the value of a
deterministic policy $\pi : S \to A$ and $V^*$ for the optimal value. If $V^\pi \ne V^*$, then the
improved policy $\pi'$ satisfies $V^{\pi'} \ne V^\pi$ (as functions on $S$).

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.policyValue_improve_ne`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/PolicyIteration.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/PolicyIteration.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/policy-iteration/index.html#policy-value-improve-ne).

## Policy iteration never decreases the value

Let $M$ be a Markov decision process with a
finite set of states $S$, a finite nonempty set of actions $A$, real rewards and stochastic
transition probabilities, and let $0 \le \gamma < 1$. Write $V^\pi$ for the value of a
deterministic policy $\pi : S \to A$, and $\pi_k$ for the policy after $k$ steps of policy
iteration from $\pi$. If $i \le j$, then $V^{\pi_i}(s) \le V^{\pi_j}(s)$ for every state $s$.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.policyValue_policyIteration_mono`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/PolicyIteration.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/PolicyIteration.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/policy-iteration/index.html#policy-value-policy-iteration-mono).

## Once optimal, policy iteration stays optimal

Let $M$ be a Markov decision process with a
finite set of states $S$, a finite nonempty set of actions $A$, real rewards and stochastic
transition probabilities, and let $0 \le \gamma < 1$. Write $V^\pi$ for the value of a
deterministic policy $\pi : S \to A$, $V^*$ for the optimal value, and $\pi_k$ for the policy
after $k$ steps of policy iteration from $\pi$. If $i \le j$ and $V^{\pi_i} = V^*$, then
$V^{\pi_j} = V^*$.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.policyValue_policyIteration_of_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/PolicyIteration.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/PolicyIteration.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/policy-iteration/index.html#policy-value-policy-iteration-of-eq).

## Policy iteration terminates

Let $M$ be a Markov decision process with a finite set of
states $S$, a finite nonempty set of actions $A$, real rewards and stochastic transition
probabilities, and let $0 \le \gamma < 1$. Write $V^\pi$ for the value of a deterministic policy
$\pi : S \to A$, $V^*$ for the optimal value, and $N = |A|^{|S|}$ for the number of deterministic
policies. For every deterministic policy $\pi$, the policy $\pi_N$ obtained after $N$ steps of
policy iteration from $\pi$ is optimal: $V^{\pi_N} = V^*$.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.policyValue_policyIteration`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/PolicyIteration.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/PolicyIteration.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/policy-iteration/index.html#policy-value-policy-iteration).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Policy iteration](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/policy-iteration/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/heuristic-search-and-planning/policy-iteration)
