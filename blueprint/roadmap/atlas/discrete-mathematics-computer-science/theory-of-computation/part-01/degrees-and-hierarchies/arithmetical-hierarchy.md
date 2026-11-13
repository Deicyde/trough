---
declaration: section
origin: cited
lean: Cslib.Decidability.IsDelta, Cslib.Decidability.computablePred_comp, Cslib.Decidability.computable_unpair_fst, Cslib.Decidability.computable_unpair_snd, Cslib.Decidability.computable_pair, Cslib.Decidability.computablePred_comp_prod, Cslib.Decidability.comp_closure, Cslib.Decidability.sigma_subset_pi_succ
statement: formalized
proof: formalized
---

# Arithmetical hierarchy

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/arithmetical-hierarchy/index.html).

## The class Δₙ of the arithmetical hierarchy

Let $n$ be a natural number. A set $P$ of
natural numbers is in $\Delta_n$ when it is in both classes $\Sigma_n$ and $\Pi_n$ of the
arithmetical hierarchy.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Definition 4.1.

Formalized by `Cslib.Decidability.IsDelta`, a definition declared in [CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/arithmetical-hierarchy/index.html#is-delta).

## Computable predicates are closed under computable precomposition

If $P$ is a decidable
set of natural numbers and $g : \mathbb{N} \to \mathbb{N}$ is a computable function, then the set
$\{w \in \mathbb{N} : g(w) \in P\}$ is decidable.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Lemma 4.2.

Formalized by `Cslib.Decidability.computablePred_comp`, a theorem declared in [CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/arithmetical-hierarchy/index.html#computable-pred-comp).

## The first projection of the pairing function is computable

Let
$\langle a, b \rangle$ denote the pairing bijection $\mathbb{N} \times \mathbb{N} \to \mathbb{N}$,
$\langle a, b \rangle = b^2 + a$ if $a < b$ and $\langle a, b \rangle = a^2 + a + b$ otherwise.
The function sending $z \in \mathbb{N}$ to the first component $a$ of the unique pair $(a, b)$
with $\langle a, b \rangle = z$ is computable.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.3.

Formalized by `Cslib.Decidability.computable_unpair_fst`, a theorem declared in [CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/arithmetical-hierarchy/index.html#computable-unpair-fst).

## The second projection of the pairing function is computable

Let
$\langle a, b \rangle$ denote the pairing bijection $\mathbb{N} \times \mathbb{N} \to \mathbb{N}$,
$\langle a, b \rangle = b^2 + a$ if $a < b$ and $\langle a, b \rangle = a^2 + a + b$ otherwise.
The function sending $z \in \mathbb{N}$ to the second component $b$ of the unique pair $(a, b)$
with $\langle a, b \rangle = z$ is computable.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.3.

Formalized by `Cslib.Decidability.computable_unpair_snd`, a theorem declared in [CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/arithmetical-hierarchy/index.html#computable-unpair-snd).

## The pairing function is computable

The pairing bijection
$\langle \cdot, \cdot \rangle : \mathbb{N} \times \mathbb{N} \to \mathbb{N}$, given by
$\langle a, b \rangle = b^2 + a$ if $a < b$ and $\langle a, b \rangle = a^2 + a + b$ otherwise,
is a computable function of its two arguments.

## Sources

- Rogers, *Theory of Recursive Functions and Effective Computability*, §1.3.

Formalized by `Cslib.Decidability.computable_pair`, a theorem declared in [CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/arithmetical-hierarchy/index.html#computable-pair).

## Computable predicates are closed under precomposition with pairing

Let
$\langle a, b \rangle$ denote the pairing bijection $\mathbb{N} \times \mathbb{N} \to \mathbb{N}$,
$\langle a, b \rangle = b^2 + a$ if $a < b$ and $\langle a, b \rangle = a^2 + a + b$ otherwise.
If $Q$ is a decidable set of natural numbers, then the set of pairs
$(a, b) \in \mathbb{N} \times \mathbb{N}$ with $\langle a, b \rangle \in Q$ is decidable.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Lemma 4.2.

Formalized by `Cslib.Decidability.computablePred_comp_prod`, a theorem declared in [CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/arithmetical-hierarchy/index.html#computable-pred-comp-prod).

## The hierarchy is closed under computable precomposition

Let $n$ be a natural number
and let $g : \mathbb{N} \to \mathbb{N}$ be computable. If a set $P$ of natural numbers is in
the class $\Sigma_n$ of the arithmetical hierarchy, then so is $\{w \in \mathbb{N} : g(w) \in P\}$;
and if $P$ is in the class $\Pi_n$, then so is $\{w \in \mathbb{N} : g(w) \in P\}$.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Lemma 4.2.

Formalized by `Cslib.Decidability.comp_closure`, a theorem declared in [CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/arithmetical-hierarchy/index.html#comp-closure).

## Every Σₙ predicate is Πₙ₊₁

Let $\Sigma_n$ and $\Pi_n$ be the levels of the arithmetical
hierarchy of predicates on $\mathbb{N}$: $\Sigma_0 = \Pi_0$ is the class of computable predicates,
$P \in \Sigma_{n+1}$ when for some $Q \in \Pi_n$ and all $x$, $P(x)$ holds iff
$Q(\langle x, y \rangle)$ holds for some $y$, and $P \in \Pi_{n+1}$ when for some $Q \in \Sigma_n$
and all $x$, $P(x)$ holds iff $Q(\langle x, y \rangle)$ holds for all $y$; here
$\langle x, y \rangle$ is the standard pairing function of $\mathbb{N}$. Then for every $n$, every
predicate in $\Sigma_n$ is in $\Pi_{n+1}$.

The proof adds a dummy universal quantifier.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Theorem 4.3.

Formalized by `Cslib.Decidability.sigma_subset_pi_succ`, a theorem declared in [CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/arithmetical-hierarchy/index.html#sigma-subset-pi-succ).

## Every Πₙ set is Σₙ₊₁

For every natural number $n$, every set of natural numbers in the
class $\Pi_n$ of the arithmetical hierarchy is also in $\Sigma_{n+1}$; that is,
$\Pi_n \subseteq \Sigma_{n+1}$, by adding a dummy existential quantifier.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Theorem 4.3.

Formalized by `Cslib.Decidability.pi_subset_sigma_succ`, a theorem declared in [CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/arithmetical-hierarchy/index.html#pi-subset-sigma-succ).

## Monotonicity of the hierarchy

For every natural number $n$, writing $\Sigma_n$ and $\Pi_n$
for the classes of the arithmetical hierarchy, every $\Sigma_n$ set of natural numbers is in
$\Sigma_{n+1}$ and every $\Pi_n$ set of natural numbers is in $\Pi_{n+1}$.

The two inclusions are proved together by induction on $n$: the step case of each uses the
other at the previous level.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Theorem 4.3.

Formalized by `Cslib.Decidability.mono_aux`, a theorem declared in [CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/arithmetical-hierarchy/index.html#mono-aux).

## Every Σₙ predicate is Σₙ₊₁

Let $\Sigma_n$ and $\Pi_n$ be the levels of the arithmetical
hierarchy of predicates on $\mathbb{N}$: $\Sigma_0 = \Pi_0$ is the class of computable predicates,
$P \in \Sigma_{n+1}$ when for some $Q \in \Pi_n$ and all $x$, $P(x)$ holds iff
$Q(\langle x, y \rangle)$ holds for some $y$, and $P \in \Pi_{n+1}$ when for some $Q \in \Sigma_n$
and all $x$, $P(x)$ holds iff $Q(\langle x, y \rangle)$ holds for all $y$; here
$\langle x, y \rangle$ is the standard pairing function of $\mathbb{N}$. Then for every $n$, every
predicate in $\Sigma_n$ is in $\Sigma_{n+1}$.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Theorem 4.3.

Formalized by `Cslib.Decidability.sigma_mono`, a theorem declared in [CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/arithmetical-hierarchy/index.html#sigma-mono).

## Monotonicity of the Π hierarchy

For every natural number $n$, every set of natural
numbers in the class $\Pi_n$ of the arithmetical hierarchy is also in $\Pi_{n+1}$; that is,
$\Pi_n \subseteq \Pi_{n+1}$.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Theorem 4.3.

Formalized by `Cslib.Decidability.pi_mono`, a theorem declared in [CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/arithmetical-hierarchy/index.html#pi-mono).

## Σₙ and Πₙ predicates are Δₙ₊₁

Let $\Sigma_n$ and $\Pi_n$ be the levels of the arithmetical
hierarchy of predicates on $\mathbb{N}$: $\Sigma_0 = \Pi_0$ is the class of computable predicates,
$P \in \Sigma_{n+1}$ when for some $Q \in \Pi_n$ and all $x$, $P(x)$ holds iff
$Q(\langle x, y \rangle)$ holds for some $y$, and $P \in \Pi_{n+1}$ when for some $Q \in \Sigma_n$
and all $x$, $P(x)$ holds iff $Q(\langle x, y \rangle)$ holds for all $y$; here
$\langle x, y \rangle$ is the standard pairing function of $\mathbb{N}$. Then for every $n$, every
predicate in $\Sigma_n$ or in $\Pi_n$ is in $\Delta_{n+1}$, that is, in both $\Sigma_{n+1}$ and
$\Pi_{n+1}$.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Theorem 4.3.

Formalized by `Cslib.Decidability.sigma_pi_subset_delta_succ`, a theorem declared in [CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/arithmetical-hierarchy/index.html#sigma-pi-subset-delta-succ).

## Σ₁ is the class of recursively enumerable predicates

A predicate $P$ on $\mathbb{N}$ is
recursively enumerable if and only if it is in $\Sigma_1$, that is, if and only if there is a
computable predicate $Q$ on $\mathbb{N}$ such that for all $x$, $P(x)$ holds iff
$Q(\langle x, y \rangle)$ holds for some $y$, where $\langle x, y \rangle$ is the standard pairing
function of $\mathbb{N}$.

This is the first level of Post's theorem.

## Sources

- Soare, *Recursively Enumerable Sets and Degrees*, Ch. I, Theorem 4.4 (Post).

Formalized by `Cslib.Decidability.sigma_one_eq_re`, a theorem declared in [CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Decidability/ArithmeticalHierarchy.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/arithmetical-hierarchy/index.html#sigma-one-eq-re).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arithmetical hierarchy](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/degrees-and-hierarchies/arithmetical-hierarchy/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/degrees-and-hierarchies/arithmetical-hierarchy)
