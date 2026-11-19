---
declaration: definition
origin: cited
lean: Prover, ProverState, ProverInput, ProverRound, ProverOutput
statement: formalized
---

# Type Signature of a Prover

A prover $\mathcal{P}$ in a reduction consists of the following components:

- **Prover State**: A family of types $\mathsf{PrvState} : \mathsf{Fin}(n+1) \to \mathsf{Type}$ representing the prover's internal state at each round of the protocol.

- **Input Processing**: A function

    $$
    \mathsf{input} : \mathsf{StmtIn} \to \mathsf{WitIn} \to \mathsf{PrvState}(0)
    $$

    that initializes the prover's state from the input statement and witness.

- **Message Sending**: For each message index $i : \mathsf{pSpec}.\mathsf{MessageIdx}$, a function

    $$
    \mathsf{sendMessage}_i : \mathsf{PrvState}(i.\mathsf{val}.\mathsf{castSucc}) \to \mathsf{OracleComp}(\mathsf{oSpec}, \mathsf{pSpec}.\mathsf{Message}(i) \times \mathsf{PrvState}(i.\mathsf{val}.\mathsf{succ}))
    $$

    that generates the message and updates the prover's state.

- **Challenge Processing**: For each challenge index $i : \mathsf{pSpec}.\mathsf{ChallengeIdx}$, a function

    $$
    \mathsf{receiveChallenge}_i : \mathsf{PrvState}(i.\mathsf{val}.\mathsf{castSucc}) \to \mathsf{OracleComp}(\mathsf{oSpec}, \mathsf{pSpec}.\mathsf{Challenge}(i) \to \mathsf{PrvState}(i.\mathsf{val}.\mathsf{succ}))
    $$

    Before seeing the challenge, the prover runs an oracle computation that returns a state-update function; applying it to the challenge gives the next state.

- **Output Generation**: A function

    $$
    \mathsf{output} : \mathsf{PrvState}(\mathsf{Fin}.\mathsf{last}(n)) \to \mathsf{OracleComp}(\mathsf{oSpec}, \mathsf{StmtOut} \times \mathsf{WitOut})
    $$

    that produces the final output statement and witness from the prover's final state. It may query the shared oracle.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Prover`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Prover), [`ProverState`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProverState), [`ProverInput`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProverInput), [`ProverRound`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProverRound), [`ProverOutput`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProverOutput).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 167](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L167)
