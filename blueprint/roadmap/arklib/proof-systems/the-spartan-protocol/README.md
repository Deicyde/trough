# The Spartan Protocol

## Preliminaries

The Spartan protocol is designed to prove the satisfiability of Rank-1 Constraint System (R1CS). An R1CS instance is defined by a set of matrices $(A, B, C)$ over a field $\mathbb{F}$ (more generally the definition makes sense over any semiring $\mathsf{R}$), and it is satisfied by a public input $x$ and a private witness $w$ if the combined vector $z = (x, w)$ satisfies the relation:

$$
(A \cdot z) \circ (B \cdot z) = (C \cdot z)
$$

where $\circ$ denotes the Hadamard (entry-wise) product. Our formalization follows the definition in `ArkLib/ProofSystem/ConstraintSystem/R1CS.lean`.

## Description in Paper

Figure 1 is the description of the Spartan protocol from the original paper (Setty 2020). Note that in this section, we only formalize the *Polynomial IOP (PIOP)* aspect of Spartan. In the PIOP model, the prover does not commit to polynomials using a Polynomial Commitment Scheme (PCS). Instead, the verifier is given oracle access to the polynomials. Therefore, steps involving ‘PCS.Setup‘, ‘PCS.Commit‘, and ‘PCS.Eval‘ are replaced by simple oracle interactions.

**Figure 1.** The Spartan protocol description, from the original paper. *(The picture is not reproduced here.)*

After stripping away the polynomial commitment scheme, the protocol has the following structure:

- **Setup:** This step is part of the polynomial commitment scheme and is not part of the PIOP we formalize.

- **Interaction:** The interaction is between a prover $\mathcal{P}$ with witness $w$ and a verifier $\mathcal{V}$ with public inputs $(\mathbb{F}, A, B, C, \text{io}, m, n)$.

    1. $\mathcal{P}$: Sends oracle access to the multilinear extension of the witness, $\tilde{w}$, to $\mathcal{V}$. In the original paper, this is a commitment $(C,S) \leftarrow \text{PC.Commit}(\text{pp}, \tilde{w})$.
    2. $\mathcal{V}$: Samples a random challenge $\tau \in \mathbb{F}^{\log m}$ and sends it to $\mathcal{P}$.
    3. Let $T_1 = 0$, $\mu_1 = \log m$, $\ell_1 = 3$. These are parameters for the first sum-check protocol.
    4. $\mathcal{V}$: Samples a random challenge $r_x \in \mathbb{F}^{\mu_1}$.
    5. **Sum-check\#1.** A sum-check protocol is executed. The verifier receives the claimed evaluation $e_x$. The prover of the sum-check has oracle access to a polynomial $G_{io, \tau}$, and the verifier has oracle access to $r_x$. The parameters for this sub-protocol are $(\mu_1, \ell_1, T_1)$.
    6. $\mathcal{P}$: Computes evaluations $v_A = \tilde{A}(r_x)$, $v_B = \tilde{B}(r_x)$, $v_C = \tilde{C}(r_x)$ and sends them to $\mathcal{V}$. $\tilde{A}, \tilde{B}, \tilde{C}$ are multilinear extensions of the matrices $A, B, C$.
    7. $\mathcal{V}$: Aborts if $e_x \neq (v_A \cdot v_B - v_C) \cdot \tilde{\text{eq}}(r_x, \tau)$. This is the verifier's check for the first sum-check.
    8. $\mathcal{V}$: Samples random challenges $r_A, r_B, r_C \in \mathbb{F}$ and sends them to $\mathcal{P}$.
    9. Let $T_2 = r_A \cdot v_A + r_B \cdot v_B + r_C \cdot v_C$, $\mu_2 = \log n$, $\ell_2 = 2$. These are parameters for the second sum-check protocol. Note: The image states $\mu_2 = \log m$, which is likely a typo and should be $\log n$.
    10. $\mathcal{V}$: Samples a random challenge $r_y \in \mathbb{F}^{\mu_2}$.
    11. **Sum-check\#2.** Another sum-check protocol is executed. The verifier receives the claimed evaluation $e_y$.
    12. $\mathcal{P}$: Computes $v \leftarrow \tilde{w}(r_y[1..])$ and sends $v$ to $\mathcal{V}$.
    13. This step involves a polynomial commitment evaluation proof. In our PIOP formalization, this check is not needed as the verifier has direct oracle access to $\tilde{w}$.
    14. $\mathcal{V}$: This step is part of the evaluation proof check, so it is omitted.
    15. $\mathcal{V}$: Computes $v_Z \leftarrow (1 - r_y[0]) \cdot \tilde{w}(r_y[1..]) + r_y[0] \cdot \widetilde{(\text{io}, 1)}(r_y[1..])$. This reconstructs the evaluation of the combined input-witness vector polynomial $\tilde{z}$.
    16. $\mathcal{V}$: Queries oracles for $\tilde{A}, \tilde{B}, \tilde{C}$ at $(r_x, r_y)$ to get $v_1, v_2, v_3$.
    17. $\mathcal{V}$: Aborts if $e_y \neq (r_A \cdot v_1 + r_B \cdot v_2 + r_C \cdot v_3) \cdot v_Z$. This is the final check.
    18. $\mathcal{V}$: Outputs 1.

## Formalization using IOR Composition

We fix an R1CS size with $m$ constraints, $n_x$ public inputs and $n_w$ witness variables, and set

$$
s = \lceil \log_2 m \rceil, \qquad t = \lceil \log_2 \max(n_x, n_w) \rceil + 1.
$$

The formalized PIOP pads the instance to $2^s$ constraints and to public-input and witness vectors of length $2^{t-1}$, so that $z = (x, w)$ is indexed by $\{0,1\}^t$. It is the sequential composition of seven oracle reductions; the bound in brackets is the round-by-round knowledge error charged to each challenge of that stage, where $q = |\mathbb{F}|$.

- [Spartan PIOP](def-spartan-reduction.md)
- [Perfect completeness](thm-spartan-completeness.md)
- [Round-by-round knowledge soundness](thm-spartan-rbr.md)
- [Knowledge soundness](thm-spartan-knowledge-soundness.md)
