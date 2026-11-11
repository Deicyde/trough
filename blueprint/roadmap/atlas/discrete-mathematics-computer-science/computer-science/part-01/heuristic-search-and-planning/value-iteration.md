---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.MarkovDecision.MDP, Cslib.Algorithms.Lean.MarkovDecision.MDP.Stochastic, Cslib.Algorithms.Lean.MarkovDecision.qValue, Cslib.Algorithms.Lean.MarkovDecision.bellman, Cslib.Algorithms.Lean.MarkovDecision.policyBellman, Cslib.Algorithms.Lean.MarkovDecision.valueIteration, Cslib.Algorithms.Lean.MarkovDecision.valueIterationVec, Cslib.Algorithms.Lean.MarkovDecision.greedy
statement: formalized
proof: formalized
---

# Value iteration

24 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html).

## Markov decision process

A Markov decision process with states in $S$, actions in $A$ and
values in $K$ consists of a reward $r(s, a) \in K$ for taking action $a$ in state $s$ and, for all
states $s, s'$ and actions $a$, a value $p(s, a, s') \in K$, the probability of moving from $s$ to
$s'$ under action $a$.

No condition is imposed here: finiteness of the states and actions, an order on $K$ and the
stochasticity of $p$ are hypotheses of the results that use them.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.MDP`, a structure declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#mdp).

## Stochastic Markov decision process

A Markov decision process with finitely many states
and transition probabilities $P(s,a,s')$ in a field $K$ with a linear order is stochastic when
$0 \le P(s,a,s')$ for all states $s, s'$ and actions $a$, and
$\sum_{s'} P(s,a,s') = 1$ for every state $s$ and action $a$.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.MDP.Stochastic`, a definition declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#stochastic).

## Q-value of an action

Let $M$ be a Markov decision process with a finite set of states
$S$ and with rewards $r(s,a)$ and transition probabilities $P(s,a,s')$ in a field $K$, and let
$\gamma \in K$. The Q-value of action $a$ in state $s$ against a value estimate
$V : S \to K$ is $r(s,a) + \gamma \sum_{s'} P(s,a,s') \, V(s')$.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.qValue`, a definition declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#q-value).

## Bellman optimality operator

Let $M$ be a Markov decision process with finitely many
states $s$, a nonempty finite set of actions $a$, rewards $r(s, a)$ and transition probabilities
$p(s, a, s')$ in a field $K$ carrying a linear order, and let $\gamma \in K$ be a discount factor.
The Bellman optimality operator $T$ sends a function $V$ from states to $K$ to the function

$$(TV)(s) = \max_a \Big( r(s, a) + \gamma \sum_{s'} p(s, a, s') V(s') \Big),$$

the largest action value in state $s$.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.bellman`, a definition declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#bellman).

## Bellman operator of a policy

Let $M$ be a Markov decision process with a finite set of
states $S$, a set of actions $A$, and rewards $r(s,a)$ and transition probabilities $P(s,a,s')$
in a field $K$, let $\gamma \in K$ be a discount factor, and let $\pi : S \to A$ be a
deterministic stationary policy. The Bellman operator of $\pi$ sends a value estimate
$V : S \to K$ to the function
$s \mapsto r(s,\pi(s)) + \gamma \sum_{s'} P(s,\pi(s),s') \, V(s')$.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.policyBellman`, a definition declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#policy-bellman).

## Value iteration

Let $M$ be a Markov decision process with finitely many states, a
nonempty finite set of actions, and rewards and transition probabilities in a field $K$ carrying
a linear order, let $\gamma \in K$, and let $T$ be the Bellman optimality operator of $M$ with
discount $\gamma$. For $n \in \mathbb{N}$ and a function $V$ from states to $K$, $n$ steps of
value iteration from $V$ give the $n$-fold iterate $T^n V$, where $T^0 V = V$.

Evaluated directly, this definition recomputes earlier iterates; tabulated value iteration
stores each update instead.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.valueIteration`, a definition declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#value-iteration).

## Tabulated value iteration

Let $M$ be a Markov decision process with states
$\{0, \dots, m-1\}$, a nonempty finite set of actions, and rewards and transition probabilities
in a field $K$ carrying a linear order, let $\gamma \in K$, and let $T$ be the Bellman optimality
operator of $M$ with discount $\gamma$. Tabulated value iteration takes a number of steps
$n \in \mathbb{N}$ and a vector $v \in K^m$, read as a function on states: with $0$ steps it
returns $v$, and with $k + 1$ steps it computes the vector $\bigl((Tv)(0), \dots, (Tv)(m-1)\bigr)$
and then runs $k$ steps from that vector.

Each update is stored as a vector, so update $k + 1$ reads the stored values of update $k$.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.valueIterationVec`, a definition declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#value-iteration-vec).

## Greedy policy

Let $M$ be a Markov decision process with finitely many states, a nonempty
finite set of actions, and rewards $r(s, a)$ and transition probabilities $p(s, a, s')$ in a field
$K$ carrying a linear order, let $\gamma \in K$, and let $V$ be a function from states to $K$. The
greedy policy for $V$ chooses in each state $s$ an action $a$ maximizing the action value
$r(s, a) + \gamma \sum_{s'} p(s, a, s') V(s')$; when several actions attain the maximum, one of
them is fixed by choice.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.greedy`, a definition declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#greedy).

## Tabulated value iteration is correct

Let $M$ be a Markov decision process with states
$\{0, \dots, m-1\}$, a nonempty finite set of actions and values in a field $K$ with a linear
order, let $\gamma \in K$, and let $T$ be the Bellman optimality operator of $M$ with discount
$\gamma$. For every $n \in \mathbb{N}$, every vector $v \in K^m$ and every state $s$, entry $s$ of
the vector computed by $n$ steps of tabulated value iteration from $v$ equals $(T^n v)(s)$, where
$v$ is read as a function on states.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.valueIterationVec_get`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#value-iteration-vec-get).

## A policy's Bellman update is at most the optimal one

Let $M$ be a Markov decision
process with a finite set of states $S$, a finite nonempty set of actions $A$, and rewards
$r(s,a)$ and transition probabilities $P(s,a,s')$ in a field $K$ with a linear order, let
$\gamma \in K$, and let $\pi : S \to A$ be a deterministic stationary policy. For every
$V : S \to K$ and every state $s$, the Bellman operator of $\pi$ applied to $V$ is at most the
Bellman optimality operator applied to $V$ at $s$:
$r(s,\pi(s)) + \gamma \sum_{s'} P(s,\pi(s),s') \, V(s') \le
\max_a \bigl(r(s,a) + \gamma \sum_{s'} P(s,a,s') \, V(s')\bigr)$.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.policyBellman_le_bellman`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#policy-bellman-le-bellman).

## The greedy action attains the Bellman maximum

Let $M$ be a Markov decision process
with a finite set of states $S$, a finite nonempty set of actions, and rewards $r(s,a)$ and
transition probabilities $P(s,a,s')$ in a field $K$ with a linear order, and let $\gamma \in K$.
For every $V : S \to K$ and every state $s$, the action $g$ that the greedy policy for $V$
chooses in $s$ satisfies
$r(s,g) + \gamma \sum_{s'} P(s,g,s') \, V(s') =
\max_a \bigl(r(s,a) + \gamma \sum_{s'} P(s,a,s') \, V(s')\bigr)$, so its action value equals
the value of the Bellman optimality operator applied to $V$ at $s$.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.qValue_greedy`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#q-value-greedy).

## The Bellman operator contracts by $\gamma$

Let $M$ be a Markov decision process with
finitely many states, a nonempty finite set of actions, and rewards and stochastic transition
probabilities in a linearly ordered field $K$, let $\gamma \ge 0$ in $K$, and let $T$ be the
Bellman optimality operator of $M$ with discount $\gamma$. If two functions $V, W$ from states
to $K$ satisfy $|V(s) - W(s)| \le d$ for every state $s$, where $d \in K$, then
$|(TV)(s) - (TW)(s)| \le \gamma d$ for every state $s$.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.abs_bellman_sub_le`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#abs-bellman-sub-le).

## Bellman's operator is a contraction

Let $M$ be a Markov decision process with finitely
many states, a nonempty finite set of actions, real rewards and stochastic transition
probabilities, and let $0 \le \gamma < 1$. Then the Bellman optimality operator $T$ of $M$ with
discount $\gamma$, acting on real-valued functions on the states with the sup metric, is a
contraction with constant $\gamma$: for all such functions $V$ and $W$,
$\|TV - TW\|_\infty \le \gamma \|V - W\|_\infty$.

## Sources

- Puterman, Theorem 6.2.3.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.bellman_contracting`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#bellman-contracting).

## Optimal value of a discounted Markov decision process

Let $M$ be a Markov decision
process with finitely many states $S$, finitely many actions (at least one), real rewards
$r(s,a)$, and transition probabilities $P(s,a,s')$ that are nonnegative and sum to $1$ over
$s'$, and let $0 \le \gamma < 1$. The optimal value of $M$ with discount $\gamma$ is the unique
function $V^* : S \to \mathbb{R}$ that is a fixed point of the Bellman optimality operator, that
is, $V^*(s) = \max_a \bigl(r(s,a) + \gamma \sum_{s'} P(s,a,s') \, V^*(s')\bigr)$ for every
state $s$. It exists and is unique because this operator is a $\gamma$-contraction in the sup
metric.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.optimalValue`, a definition declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#optimal-value).

## Value of a policy

Let $M$ be a Markov decision process with a finite set of states $S$,
a set of actions $A$, real rewards $r(s,a)$, and transition probabilities $P(s,a,s')$ that are
nonnegative and sum to $1$ over $s'$, let $0 \le \gamma < 1$, and let $\pi : S \to A$ be a
deterministic stationary policy. The value of $\pi$ is the unique function
$V^\pi : S \to \mathbb{R}$ that is a fixed point of the Bellman operator of $\pi$, that is,
$V^\pi(s) = r(s,\pi(s)) + \gamma \sum_{s'} P(s,\pi(s),s') \, V^\pi(s')$ for every state $s$.
It exists and is unique because this operator is a $\gamma$-contraction in the sup metric.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.policyValue`, a definition declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#policy-value).

## The optimal value solves the Bellman optimality equation

Let $M$ be a Markov decision
process with finitely many states, a nonempty finite set of actions, real rewards and stochastic
transition probabilities, and let $0 \le \gamma < 1$. Then the optimal value $V^*$ of $M$ with
discount $\gamma$ is a fixed point of the Bellman optimality operator $T$ of $M$ with discount
$\gamma$: $T V^* = V^*$.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.bellman_optimalValue`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#bellman-optimal-value).

## Uniqueness of the solution of the Bellman optimality equation

Let $M$ be a Markov
decision process with finitely many states, a nonempty finite set of actions, real rewards and
stochastic transition probabilities, and let $0 \le \gamma < 1$. If a real-valued function $V$ on
the states satisfies $TV = V$, where $T$ is the Bellman optimality operator of $M$ with discount
$\gamma$, then $V$ is the optimal value of $M$ with discount $\gamma$.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.eq_optimalValue_of_bellman_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#eq-optimal-value-of-bellman-eq).

## A policy's value satisfies its Bellman equation

Let $M$ be a Markov decision process
with finitely many states, real rewards $r(s,a)$, and transition probabilities $P(s,a,s')$ that
are nonnegative and sum to $1$ over $s'$, let $0 \le \gamma < 1$, and let $\pi$ be a
deterministic stationary policy with value $V^\pi$. Then $V^\pi$ is a fixed point of the
Bellman operator of $\pi$: for every state $s$,
$V^\pi(s) = r(s,\pi(s)) + \gamma \sum_{s'} P(s,\pi(s),s') \, V^\pi(s')$.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.policyBellman_policyValue`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#policy-bellman-policy-value).

## Uniqueness of the solution of a policy's Bellman equation

Let $M$ be a Markov decision
process with finitely many states, real rewards and stochastic transition probabilities, let
$0 \le \gamma < 1$, and let $\pi$ be a deterministic stationary policy, a map from states to
actions. If a real-valued function $V$ on the states satisfies $T_\pi V = V$, where $T_\pi$ is the
Bellman operator of $\pi$ in $M$ with discount $\gamma$, then $V$ is the value of $\pi$.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.eq_policyValue_of_policyBellman_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#eq-policy-value-of-policy-bellman-eq).

## Value iteration converges

Let $M$ be a Markov decision process with finitely many states
$S$, a nonempty finite set of actions, real rewards and stochastic transition probabilities
(nonnegative, each row summing to $1$), and let $0 \le \gamma < 1$ be a discount factor. Let $T$ be
the Bellman optimality operator of $M$ with discount $\gamma$. Then for every initial value
function $V : S \to \mathbb{R}$, the value iterates $T^n V$ converge to the optimal value of $M$
with discount $\gamma$ as $n \to \infty$.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.tendsto_valueIteration`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#tendsto-value-iteration).

## A priori error bound for value iteration

Let $M$ be a Markov decision process with
finitely many states, a nonempty finite set of actions, real rewards and stochastic transition
probabilities, let $0 \le \gamma < 1$, and let $T$ be the Bellman optimality operator and $V^*$
the optimal value of $M$ with discount $\gamma$. For every real-valued function $V$ on the states
and every $n \in \mathbb{N}$, the result $T^n V$ of $n$ steps of value iteration from $V$ satisfies
$\|T^n V - V^*\|_\infty \le \|V - TV\|_\infty \, \gamma^n / (1 - \gamma)$, where
$\|\cdot\|_\infty$ is the sup norm.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.dist_valueIteration_le`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#dist-value-iteration-le).

## Stopping test

Let $M$ be a Markov decision process with finitely many states,
a nonempty finite set of actions, real rewards and stochastic transition probabilities, let
$0 \le \gamma < 1$, and let $T$ be the Bellman optimality operator and $V^*$ the optimal value of
$M$ with discount $\gamma$. For every real-valued function $V$ on the states,
$\|V - V^*\|_\infty \le \|V - TV\|_\infty / (1 - \gamma)$, where $\|\cdot\|_\infty$ is the sup
norm. So if one Bellman update moves $V$ by at most $\varepsilon$, then $V$ is within
$\varepsilon / (1 - \gamma)$ of the optimal value.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.dist_optimalValue_le`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#dist-optimal-value-le).

## No policy beats the optimal value

Let $M$ be a Markov decision process with finitely
many states, finitely many actions (at least one), real rewards $r(s,a)$, and transition
probabilities $P(s,a,s')$ that are nonnegative and sum to $1$ over $s'$, and let
$0 \le \gamma < 1$. For every deterministic stationary policy $\pi$, the value $V^\pi$ of $\pi$
is at most the optimal value $V^*$ in every state: $V^\pi(s) \le V^*(s)$ for all states $s$.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.policyValue_le_optimalValue`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#policy-value-le-optimal-value).

## A greedy policy for the optimal value is optimal

Let $M$ be a Markov decision process
with finitely many states, finitely many actions (at least one), real rewards $r(s,a)$, and
transition probabilities $P(s,a,s')$ that are nonnegative and sum to $1$ over $s'$, let
$0 \le \gamma < 1$, and let $V^*$ be the optimal value. Let $\pi$ be the greedy policy for
$V^*$, which in each state $s$ chooses an action $a$ maximizing
$r(s,a) + \gamma \sum_{s'} P(s,a,s') \, V^*(s')$. Then the value of $\pi$ equals $V^*$.

Formalized by `Cslib.Algorithms.Lean.MarkovDecision.policyValue_greedy`, a theorem declared in [CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/MDP/ValueIteration.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html#policy-value-greedy).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Value iteration](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/heuristic-search-and-planning/value-iteration)
