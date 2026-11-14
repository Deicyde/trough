---
declaration: definition
origin: cited
lean: OracleVerifier.toVerifier
statement: formalized
---

# Oracle Verifier to Verifier Conversion

An oracle verifier can be converted to a standard verifier through a natural simulation process. The key insight is that while an oracle verifier only has oracle access to certain data (input oracle statements and prover messages), a standard verifier can be given the actual underlying data directly.

The conversion works as follows: when the oracle verifier needs to make an oracle query to some data, the converted verifier can respond to this query immediately using the actual underlying data it possesses. This is accomplished through the `OracleInterface` type class, which specifies for each data type how to respond to queries given the underlying data.

Specifically, given an oracle verifier $\mathcal{V}_{\text{oracle}}$:

- The converted verifier $\mathcal{V}_{\text{oracle}}.\mathsf{toVerifier}$ takes as input both the statement *and* the actual underlying data for all oracle statements
- When $\mathcal{V}_{\text{oracle}}$ attempts to query an oracle statement or prover message, the converted verifier uses the corresponding `OracleInterface` instance to compute the response from the actual data
- The output oracle statements are the materialized output: in the embedding case, the selected input oracle statements and prover messages; in the virtual case, the value of $\mathsf{materializeOutput}$ on the challenges, input oracle data and messages
- If the oracle verifier rejects, so does the converted verifier

## Depends on

- [Type Signature of an Oracle Verifier](def-oracle-verifier.md)

## Lean

Formalized as [`OracleVerifier.toVerifier`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OracleVerifier.toVerifier).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 263](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L263)
