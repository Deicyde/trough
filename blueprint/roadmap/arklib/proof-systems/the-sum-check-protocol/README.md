# The Sum-Check Protocol

This section documents our formalization of the sum-check protocol. We first describe the sum-check protocol as it is typically described in the literature, and then present a modular description that maximally relies on our general oracle reduction framework.

## Standard Description

### Protocol Parameters

The sum-check protocol is parameterized by the following:

- $R$: the underlying ring (for soundness, required to be finite and an integral domain)
- $n \in \mathbb{N}$: the number of variables (and the number of rounds for the protocol)
- $d \in \mathbb{N}$: the individual degree bound for the polynomial
- $\mathcal{D}: \{0, 1, \ldots, m-1\} \hookrightarrow R$: the set of $m$ evaluation points for each variable, represented as an injection. The image of $\mathcal{D}$ as a finite subset of $R$ is written as $\text{Image}(\mathcal{D})$.
- $\mathcal{O}$: the set of underlying oracles (e.g., random oracles) that may be needed for other reductions. However, the sum-check protocol itself does *not* use any oracles.

### Input and Output Statements

For the standard description of the sum-check protocol, we specify the complete input and output data:

Input Statement. The claimed sum $T \in R$.

Input Oracle Statement. The polynomial $P \in R[X_0, X_1, \ldots, X_{n-1}]_{\leq d}$ of $n$ variables with bounded individual degrees $d$.

Input Witness. None (the unit type).

Input Relation. The sum-check relation:

$$
\sum_{x \in (\text{Image}(\mathcal{D}))^n} P(x) = T
$$

Output Statement. The claimed evaluation $e \in R$ and the challenge vector $(r_0, r_1, \ldots, r_{n-1}) \in R^n$.

Output Oracle Statement. The same polynomial $P \in R[X_0, X_1, \ldots, X_{n-1}]_{\leq d}$.

Output Witness. None (the unit type).

Output Relation. The evaluation relation:

$$
P(r_0, r_1, \ldots, r_{n-1}) = e
$$

### Protocol Description

The sum-check protocol proceeds in $n$ rounds of interaction between the prover and verifier. The protocol reduces the claim that a multivariate polynomial $P$ sums to a target value $T$ over the domain $(\text{Image}(\mathcal{D}))^n$ to the claim that $P$ evaluates to a specific value $e$ at a random point $(r_0, r_1, \ldots, r_{n-1})$.

In each round, the prover sends a univariate polynomial of bounded degree, and the verifier responds with a random challenge. The verifier performs consistency checks by querying the polynomial oracle at specific evaluation points. After $n$ rounds, the protocol terminates with an output statement asserting that $P(r_0, r_1, \ldots, r_{n-1}) = e$, where the challenges $(r_0, r_1, \ldots, r_{n-1})$ are the random values chosen by the verifier during the protocol execution.

The protocol is described as an oracle reduction, where the polynomial $P$ is accessed only through evaluation queries rather than being explicitly represented.

### Security Properties

We prove the following security properties for the sum-check protocol:

- [Perfect Completeness](thm-sumcheck-perfect-completeness.md)
- [Round-by-Round Knowledge Soundness](thm-sumcheck-rbr-knowledge-soundness-standard.md)
- [Knowledge Soundness](thm-sumcheck-knowledge-soundness.md)

### Implementation Notes

Our formalization includes several important implementation considerations:

Oracle Reduction Level. This description of the sum-check protocol stays at the **oracle reduction** level, describing the protocol before being compiled with concrete cryptographic primitives such as polynomial commitment schemes for $P$. The oracle model allows us to focus on the logical structure and security properties of the protocol without being concerned with the specifics of how polynomial evaluations are implemented or verified.

Abstract Protocol Description. The protocol description above does not consider implementation details and optimizations that would be necessary in practice. For instance, we do not address computational efficiency, concrete polynomial representations, or specific algorithms for polynomial evaluation. This abstraction allows us to establish the fundamental security properties that any concrete implementation must preserve.

Degree Constraints. To represent sum-check as a series of Interactive Oracle Reductions (IORs), we implicitly constrain the degree of the polynomials via using subtypes such as $R[X]_{\leq d}$ and appropriate multivariate polynomial degree bounds. This is necessary because the oracle verifier only gets oracle access to evaluating the polynomials, but does not see the polynomials in the clear.

Polynomial Commitments. When this protocol is compiled to an interactive proof (rather than an oracle reduction), the corresponding polynomial commitment schemes will enforce that the declared degree bounds hold, by letting the (non-oracle) verifier perform explicit degree checks.

### Generalizations Not Covered

The formalized sum-check does not cover the following generalizations; `ROADMAP.md` tracks planned protocol work.

- **Variable Degree Bounds:** Generalize to $d : \{0, 1, \ldots, n-1\} \to \mathbb{N}$ and $\mathcal{D} : \{0, 1, \ldots, n-1\} \to (\{0, 1, \ldots, m-1\} \hookrightarrow R)$, allowing different degree bounds and summation domains for each variable.
- **Restricted Challenge Domains:** Generalize the challenges to come from suitable subsets of $R$ (e.g., subtractive sets), rather than the entire domain. This modification is used in lattice-based protocols.
- **Module-based Sum-check:** Extend to sum-check over modules instead of just rings. This would require extending multivariate polynomial evaluation to modules, defining something like $\text{evalModule} : (R^n \to M) \to R[X_0, \ldots, X_{n-1}] \to M$ where $M$ is an $R$-module.

## Modular Description

### Round-by-Round Analysis

Our modular approach breaks down the sum-check protocol into individual rounds, each of which can be analyzed as a two-message Interactive Oracle Reduction. This decomposition allows us to prove security properties compositionally and provides a more granular understanding of the protocol's structure.

Round-Specific Statements. For the $i$-th round, where $i \in \{0, 1, \ldots, n\}$, the statement contains:

- $\text{target} \in R$: the target value for sum-check at this round
- $\text{challenges} \in R^i$: the list of challenges sent from the verifier to the prover in previous rounds

The oracle statement remains the same polynomial $P \in R[X_0, X_1, \ldots, X_{n-1}]_{\leq d}$.

Round-Specific Relations. The sum-check relation for the $i$-th round checks that:

$$
\sum_{x \in (\text{Image}(\mathcal{D}))^{n-i}} P(\text{challenges}, x) = \text{target}
$$

Note that when $i = n$, this becomes the output statement of the sum-check protocol, checking that $P(\text{challenges}) = \text{target}$.

### Individual Round Protocol

For $i = 0, 1, \ldots, n-1$, the $i$-th round of the sum-check protocol consists of the following:

Step 1: Prover's Message. The prover sends a univariate polynomial $p_i \in R[X]_{\leq d}$ of degree at most $d$. If the prover is honest, then:

$$
p_i(X) = \sum_{x \in (\text{Image}(\mathcal{D}))^{n-i-1}} P(\text{challenges}_0, \ldots, \text{challenges}_{i-1}, X, x)
$$

Here, $P(\text{challenges}_0, \ldots, \text{challenges}_{i-1}, X, x)$ is the polynomial $P$ evaluated at the concatenation of:

- the prior challenges $\text{challenges}_0, \ldots, \text{challenges}_{i-1}$
- the $i$-th variable as the new indeterminate $X$
- the remaining values $x \in (\text{Image}(\mathcal{D}))^{n-i-1}$

In the oracle protocol, this polynomial $p_i$ is turned into an oracle for which the verifier can query evaluations at arbitrary points.

Step 2: Verifier's Challenge. The verifier sends the $i$-th challenge $r_i$ sampled uniformly at random from $R$.

Step 3: Verifier's Check. The (oracle) verifier performs queries for the evaluations of $p_i$ at all points in $\text{Image}(\mathcal{D})$, and checks that:

$$
\sum_{x \in \text{Image}(\mathcal{D})} p_i(x) = \text{target}
$$

If the check fails, the verifier outputs $\texttt{failure}$. Otherwise, it outputs a statement for the next round as follows:

- $\text{target}$ is updated to $p_i(r_i)$
- $\text{challenges}$ is updated to the concatenation of the previous challenges and $r_i$

### Single Round Security Analysis

- [Single Round Protocol](def-sumcheck-single-round.md)
- [Single Round Completeness](thm-sumcheck-single-round-completeness.md)
- [Single Round Knowledge Soundness](thm-sumcheck-single-round-soundness.md)

### Virtual Protocol Decomposition

We now proceed to break down this protocol into individual messages, and then specify the predicates that should hold before and after each message is exchanged.

First, it is clear that we can consider each round in isolation. In fact, each round can be seen as an instantiation of the following simpler "virtual" protocol:

- [virtual_sumcheck_round_protocol](def-virtual-sumcheck-round-protocol.md)

The reason why this simpler protocol is related to a sum-check round is that we can *emulate* the simpler protocol using variables in the context at the time:

- The univariate polynomial $p$ is instantiated as $\sum_{x \in (\text{Image}(\mathcal{D}))^{n - i - 1}} P(r_0, \ldots, r_{i - 1}, X, x)$.
- The scalar $c$ is instantiated as $T$ if $i = 0$, and as $s_{i - 1}(r_{i - 1})$ otherwise.

The simpler protocol is perfectly complete. It is sound (and since there is no witness, also knowledge sound) since, when $R$ is an integral domain, two distinct polynomials of degree at most $d$ agree at a uniformly random $r$ with probability at most $d / |R|$; if the claim is false and $s$ passes the check, then $s \neq p$.

- [virtual_sumcheck_round_protocol_complete](thm-virtual-sumcheck-round-protocol-complete.md)

Soundness and knowledge soundness of the virtual round follow from its round-by-round knowledge soundness below, by the general implications of Section [Security Properties](../../oracle-reductions/definitions/README.md).

We use the following state function for the simpler protocol.

Seen in this light, the simpler protocol satisfies round-by-round knowledge soundness: the only challenge moves the state from false to true exactly when the initial claim is false, $s$ passes the check (so $s \neq p$), and $p(r) = s(r)$.

- [virtual_sumcheck_round_protocol_rbr_sound](thm-virtual-sumcheck-round-protocol-rbr-sound.md)

## Sum-Check in the Interaction Layer

ArkLib also formalizes sum-check in its interaction layer (`ArkLib/Interaction`), which is meant to replace the legacy layer used above, as a protocol tree whose prover strategies may keep arbitrary memory and perform effects after each challenge. The execution outputs an evaluation claim about the original oracle.

- [Interaction-layer sum-check security](thm-sumcheck-interaction.md)
