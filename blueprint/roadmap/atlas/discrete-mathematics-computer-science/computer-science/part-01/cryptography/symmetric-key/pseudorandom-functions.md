---
declaration: section
origin: cited
lean: Cslib.Crypto.PRF.prfReal, Cslib.Crypto.PRF.prfRand, Cslib.Crypto.PRF.prfAdvantage, Cslib.Crypto.PRF.MacWins, Cslib.Crypto.PRF.macGame, Cslib.Crypto.PRF.macReduction, Cslib.Crypto.PRF.macGame_eq_prfReal, Cslib.Crypto.PRF.card_macWins_mul_le
statement: formalized
proof: formalized
---

# Pseudorandom functions

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html).

## The PRF experiment

## Real world of the PRF experiment

Let $K$, $X$, $Y$ and $S$ be finite sets with $K$, $Y$
and $S$ nonempty, let $F : K \to X \to Y$ be a keyed function and let $D$ be a distinguisher: an
oracle algorithm with coins in $S$ that queries a function $X \to Y$ and outputs a bit. The real
world is the distribution of the output of $D$ with coins $s$ and oracle $F(k, \cdot)$, where the
pair $(k, s)$ is uniform on $K \times S$.

Formalized by `Cslib.Crypto.PRF.prfReal`, a definition declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#prf-real).

## Random world of the PRF experiment

Let $X$, $Y$ and $S$ be finite sets with $Y$ and $S$
nonempty, and let $D$ be a distinguisher: an oracle algorithm with coins in $S$ that queries a
function $X \to Y$ and outputs a bit. The random world is the distribution of the output of $D$
with coins $s$ and oracle $f$, where the pair $(f, s)$ is uniform on $(X \to Y) \times S$.

Formalized by `Cslib.Crypto.PRF.prfRand`, a definition declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#prf-rand).

## PRF advantage

Let $K$, $X$, $Y$ and $S$ be finite sets with $K$, $Y$ and $S$ nonempty,
let $F : K \to X \to Y$ be a keyed function and let $D$ be a distinguisher: an oracle algorithm
with coins in $S$ that queries a function $X \to Y$ and outputs a bit. The PRF advantage of $D$
against $F$ is the real number $|p_{\mathrm{real}} - p_{\mathrm{rand}}|$, where
$p_{\mathrm{real}}$ is the probability that $D$ outputs $1$ in the real world (uniform coins
$s \in S$, oracle $F(k, \cdot)$ for a uniform key $k \in K$) and $p_{\mathrm{rand}}$ is the
probability that $D$ outputs $1$ in the random world (uniform coins, oracle a uniformly random
function $X \to Y$).

Formalized by `Cslib.Crypto.PRF.prfAdvantage`, a definition declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#prf-advantage).

## Winning the forgery game

A forger $c$, an adaptive oracle algorithm with queries in $M$,
answers in $T$ and output in $M \times T$, wins against the tagging oracle $O \colon M \to T$
when, run with oracle $O$, it outputs a pair $(m, t)$ with $O(m) = t$ and $m$ is not among the
queries it asks in that run.

Formalized by `Cslib.Crypto.PRF.MacWins`, a definition declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#mac-wins).

## The MAC forgery experiment

Let $K$ and $R$ be finite nonempty types, let
$F \colon K \to M \to T$ be a keyed function, and let $A$ be a forger: for coins $r \in R$,
$A(r)$ is an adaptive oracle algorithm with queries in $M$, answers in $T$ and output in
$M \times T$. The existential-forgery experiment under an adaptive chosen-message attack for the
MAC $\mathrm{Mac}_k(m) = F(k, m)$ draws $(k, r)$ uniformly from $K \times R$, runs $A(r)$ with
the tagging oracle $F(k, \cdot)$, and outputs true exactly when $A(r)$ wins against that oracle,
that is, outputs a pair $(m, t)$ with $F(k, m) = t$ where $m$ is not among its queries.

Formalized by `Cslib.Crypto.PRF.macGame`, a definition declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#mac-game).

## The distinguisher built from a forger

For a list $L$ of messages in $M$ and a forger $c$,
an adaptive oracle algorithm with queries in $M$, answers in $T$ and output in $M \times T$, the
MAC reduction is the oracle algorithm with the same queries and answers and a Boolean output,
defined by recursion on $c$. If $c$ stops with output $(m, t)$, it queries $m$ and, on answer
$t'$, stops with output true exactly when $t' = t$ and $m \notin L$. If $c$ queries $x$ and
continues with $c_y$ on answer $y$, it queries $x$ and, on answer $y$, continues as the MAC
reduction of $c_y$ with $x$ added to $L$.

Started with the empty list, it runs the forger, logging its queries, then queries the forged
message and accepts when the answer is the forged tag and the message is fresh.

Formalized by `Cslib.Crypto.PRF.macReduction`, a definition declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#mac-reduction).

## The MAC reduction in the real PRF world

Let $K$ and $R$ be finite nonempty types, let
$F \colon K \to M \to T$ be a keyed function, and let $A$ be a forger: for coins $r \in R$,
$A(r)$ is an adaptive oracle algorithm with queries in $M$, answers in $T$ and output in
$M \times T$. Then the output distribution of the existential-forgery experiment for $F$ and $A$
equals the output distribution of the real world of the PRF experiment for $F$ with the
distinguisher that, on coins $r$, runs the MAC reduction on $A(r)$ starting from the empty query
log.

Formalized by `Cslib.Crypto.PRF.macGame_eq_prfReal`, a theorem declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#mac-game-eq-prf-real).

## Counting forgeries against a random function

Let $M$ and $T$ be finite sets and let $c$ be
an adaptive oracle algorithm that queries messages in $M$, receives tags in $T$ and outputs a pair
in $M \times T$. Call a function $f \colon M \to T$ a win for $c$ when the run of $c$ with oracle
$f$ outputs a pair $(m, t)$ with $f(m) = t$ and $m$ not among the messages queried in that run.
If $W$ is the set of functions $M \to T$ that are wins for $c$, then $|W| \cdot |T| \le |T|^{|M|}$.

Changing the tag of the fresh forged message, which the run never queries, gives $|T|$ functions
with the same run, of which exactly one is a win.

Formalized by `Cslib.Crypto.PRF.card_macWins_mul_le`, a theorem declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#card-mac-wins-mul-le).

## Forging against a random function

Let $M$ and $T$ be finite sets with $T$ nonempty, and
let $A$ be a forger: an oracle algorithm with coins in a finite nonempty set that queries tags
in $T$ of messages in $M$ and outputs a message together with a tag. When the tagging oracle is
a uniformly random function $M \to T$ and the coins are uniform, the MAC reduction built from
$A$ accepts (that is, $A$ outputs the correct tag of a message it never queried) with
probability at most $1/|T|$.

Formalized by `Cslib.Crypto.PRF.prfRand_macReduction_le`, a theorem declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#prf-rand-mac-reduction-le).

## The MAC from a PRF, concrete security

Let $K$, $M$, $T$ and $R$ be finite types with
$K$, $T$ and $R$ nonempty, let $F \colon K \to M \to T$ be a keyed function, and let $A$ be an
adaptive chosen-message forger: for coins $r \in R$, $A(r)$ is an adaptive oracle algorithm
with queries in $M$, answers in $T$ and output in $M \times T$. Then the probability that $A$
wins the existential-forgery experiment for the MAC $\mathrm{Mac}_k(m) = F(k, m)$ is at most
the PRF advantage against $F$ of the distinguisher that, on coins $r$, runs the MAC reduction
on $A(r)$ starting from the empty query log, plus $1 / |T|$.

This is the reduction of Katz and Lindell, Theorem 4.6, stated as a concrete inequality.

Formalized by `Cslib.Crypto.PRF.macGame_le`, a theorem declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#mac-game-le).

## Encryption from a keyed function

Let $Y$ be an additive commutative group of messages
and let $f \colon X \to Y$ be a function (in the scheme, $f = F_k$ for a key $k$). The
encryption of a message $m \in Y$ with randomness $r \in X$ is the pair
$(r, f(r) + m) \in X \times Y$.

This is Construction 3.30 of Katz and Lindell, with XOR replaced by the addition of the
message group.

Formalized by `Cslib.Crypto.PRF.encrypt`, a definition declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#encrypt).

## Decryption with a keyed function

For a function $F_k \colon X \to Y$ into an additive
commutative group $Y$, the decryption of a ciphertext $(r, c) \in X \times Y$ is
$\mathrm{Dec}(r, c) = c - F_k(r)$.

Formalized by `Cslib.Crypto.PRF.decrypt`, a definition declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#decrypt).

## Correctness of encryption with a keyed function

Let $Y$ be an additive commutative group
and $F_k \colon X \to Y$ a function. For every message $m \in Y$ and every randomness $r \in X$,
decrypting the ciphertext $\mathrm{Enc}(m) = (r, F_k(r) + m)$ gives back $m$, that is,
$\mathrm{Dec}(\mathrm{Enc}(m)) = m$ where $\mathrm{Dec}(r, c) = c - F_k(r)$.

Formalized by `Cslib.Crypto.PRF.decrypt_encrypt`, a theorem declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#decrypt-encrypt).

## Selecting the challenge message by a bit

Given a pair of messages
$(m_0, m_1) \in Y \times Y$ and a challenge bit $b$, the selected message is $m_1$ when $b$ is
true and $m_0$ when $b$ is false.

Formalized by `Cslib.Crypto.PRF.pick`, a definition declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#pick).

## Running an algorithm against the bounded encryption oracle

Let $X$ be a set, $Y$ an
abelian group written additively, $f : X \to Y$ a function, $q \in \mathbb{N}$ and
$\rho : \{0, \dots, q - 1\} \to X$ the encryption randomness of the queries. Run from query index
$i \in \mathbb{N}$, an oracle algorithm with messages in $Y$ as queries, answers in $X \times Y$
and outputs in $\beta$ either fails or yields its output together with the next query index: if
it stops with output $a$, the result is $(a, i)$; if it queries a message $m$ and $i < q$, the
oracle answers $(\rho(i), f(\rho(i)) + m)$ and the run continues from index $i + 1$; if it
queries a message and $i \ge q$, the run fails.

Formalized by `Cslib.Crypto.PRF.runEnc`, a definition declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#run-enc).

## CPA adversary

A CPA adversary with coins in $R$, against an encryption oracle that takes
messages in $Y$ and returns ciphertexts in $X \times Y$, assigns to each $r \in R$ an adaptive
oracle algorithm with access to the encryption oracle that outputs two challenge messages
$(m_0, m_1) \in Y \times Y$ together with a second adaptive oracle algorithm, again with access to
the encryption oracle, which takes the challenge ciphertext in $X \times Y$ and outputs a guess
for the challenge bit.

Formalized by `Cslib.Crypto.PRF.CPAAdversary`, an abbreviation declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#cpaadversary).

## The adversary's guess in the CPA experiment

Let $Y$ be an additive commutative group,
$f \colon X \to Y$ a function, $q$ a natural number, $\rho \colon \{0, \dots, q - 1\} \to X$ the
encryption randomness, $r_s \in X$ the challenge randomness and $b$ a bit. Let $c$ be an oracle
algorithm for the encryption oracle that outputs two messages $(m_0, m_1) \in Y \times Y$ and a
second-phase algorithm. The encryption query with index $i$, counting from $0$ across both
phases, is answered for a message $m$ by $(\rho_i, f(\rho_i) + m)$. Run $c$; when it outputs
$(m_0, m_1)$, run its second phase on the challenge ciphertext $(r_s, f(r_s) + m_b)$, where $m_b$
is $m_1$ if $b$ is true and $m_0$ otherwise. The guess is the output of the second phase. If the
two phases together ask more than $q$ encryption queries, the adversary is stopped and the guess
is false.

Formalized by `Cslib.Crypto.PRF.cpaGuess`, a definition declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#cpa-guess).

## The CPA experiment

Let $K$, $X$ and $R$ be nonempty finite sets, $Y$ an additive
commutative group, $q$ a natural number, $F \colon K \to X \to Y$ a keyed function and $A$ a CPA
adversary with coins in $R$. The CPA indistinguishability experiment $\mathrm{PrivK}^{\mathrm{cpa}}$
for the scheme $\mathrm{Enc}_k(m) = (r, F_k(r) + m)$ draws, uniformly and independently, a key
$k \in K$, encryption randomness $\rho \colon \{0, \dots, q - 1\} \to X$ for the encryption
queries, challenge randomness $r_s \in X$, a challenge bit $b$ and coins $r \in R$. It outputs true
exactly when the adversary's guess, with keyed function $F_k$, encryption randomness $\rho$,
challenge randomness $r_s$, challenge bit $b$ and the algorithm that $A$ assigns to $r$, equals $b$.
An adversary that asks more than $q$ encryption queries is stopped and guesses false.

Formalized by `Cslib.Crypto.PRF.cpaGame`, a definition declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#cpa-game).

## CPA advantage

Let $K$, $X$ and $R$ be nonempty finite sets, $Y$ an additive commutative
group, $q$ a natural number, $F \colon K \to X \to Y$ a keyed function and $A$ a CPA adversary
with coins in $R$. The CPA advantage of $A$ is the real number $|p - 1/2|$, where $p$ is the
probability that the CPA experiment for $F$ and $A$ with at most $q$ encryption queries outputs
true, that is, that $A$ guesses the challenge bit.

Formalized by `Cslib.Crypto.PRF.cpaAdvantage`, a definition declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#cpa-advantage).

## Simulating the encryption oracle with a function oracle

Let $X$ be a set, $Y$ an abelian
group written additively, $q \in \mathbb{N}$ and $\rho : \{0, \dots, q - 1\} \to X$ the
encryption randomness of the queries. Started at query index $i \in \mathbb{N}$, the simulation
turns an oracle algorithm with messages in $Y$ as queries, answers in $X \times Y$ and outputs in
$\beta$ into an oracle algorithm with queries in $X$ and answers in $Y$ that either fails or
outputs the original output together with the next query index: if the original algorithm stops
with output $a$, the simulation stops with $(a, i)$; if it queries a message $m$ and $i < q$, the
simulation queries $\rho(i)$ and, on answer $y$, continues by simulating the original algorithm
on the answer $(\rho(i), y + m)$ from index $i + 1$; if it queries a message and $i \ge q$, the
simulation stops with failure.

Formalized by `Cslib.Crypto.PRF.simEnc`, a definition declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#sim-enc).

## The PRF distinguisher built from a CPA adversary

Let $X$ and $R$ be sets, $Y$ an additive
commutative group, $q$ a natural number and $A$ a CPA adversary with coins in $R$ against an
encryption oracle that takes messages in $Y$ and returns ciphertexts in $X \times Y$. With its own
coins $(\rho, r_s, b, r)$, where $\rho \colon \{0, \dots, q - 1\} \to X$, $r_s \in X$, $b$ is a bit
and $r \in R$, and with oracle access to a function $O \colon X \to Y$, the distinguisher runs the
algorithm $A$ assigns to $r$. It answers the encryption query with index $i$, counting from $0$
across both phases, for a message $m$ by querying $O$ at $\rho_i$ and returning
$(\rho_i, O(\rho_i) + m)$. When the first phase outputs messages $(m_0, m_1)$, it queries $O$ at
$r_s$ and gives the second phase the challenge ciphertext $(r_s, O(r_s) + m_b)$, where $m_b$ is
$m_1$ if $b$ is true and $m_0$ otherwise. It outputs true exactly when the adversary's guess
equals $b$, where an adversary that asks more than $q$ encryption queries is stopped and guesses
false.

Formalized by `Cslib.Crypto.PRF.cpaReduction`, a definition declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#cpa-reduction).

## The CPA reduction is exact with the real oracle

Let $K$, $X$ and $R$ be nonempty finite
sets, $Y$ an additive commutative group, $q$ a natural number and $F \colon K \to X \to Y$ a keyed
function. For every CPA adversary $A$ with coins in $R$, the CPA experiment for $F$ and $A$ with
at most $q$ encryption queries has the same output distribution as the real world of the PRF
experiment for $F$ run with the distinguisher built from $A$ for $q$ queries: with the oracle $F_k$
for a uniform key $k$, the reduction runs the CPA experiment exactly.

Formalized by `Cslib.Crypto.PRF.cpaGame_eq_prfReal`, a theorem declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#cpa-game-eq-prf-real).

## The encryption oracle depends only on the encryption randomness

Let $Y$ be an additive
commutative group, let $\rho_0, \dots, \rho_{q-1} \in X$ be encryption randomness and let
$f, f' : X \to Y$ satisfy $f(\rho_j) = f'(\rho_j)$ for every $j < q$. Then for every oracle
algorithm $c$ and every natural number $i$, running $c$ against the encryption oracle built from
$f$, with query indices starting at $i$, gives the same result as running it against the one
built from $f'$. Here the encryption oracle built from $f$ answers a query $m$ with index $n < q$
by $(\rho_n, f(\rho_n) + m)$, and the run fails at a query with index $n \ge q$.

Formalized by `Cslib.Crypto.PRF.runEnc_congr`, a theorem declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#run-enc-congr).

## The CPA reduction against a random function

Let $X$ be a finite nonempty set, $Y$ a
finite additive commutative group, $q$ a natural number and $A$ a CPA adversary with coins in a
finite nonempty set. Let $p$ be the probability that the CPA reduction built from $A$ (whose
encryption oracle answers at most $q$ queries) outputs $1$, that is, that $A$ guesses the
challenge bit, when its oracle is a uniformly random function $X \to Y$ and its coins are
uniform. Then $|p - 1/2| \le q / (2|X|)$.

The success probability is exactly $1/2$ unless the challenge randomness repeats the randomness
of one of the at most $q$ encryption queries.

Formalized by `Cslib.Crypto.PRF.prfRand_cpaReduction`, a theorem declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 478](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L478). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#prf-rand-cpa-reduction).

## CPA encryption from a PRF, concrete security

Let $K$, $X$ and $R$ be nonempty finite sets,
$Y$ a finite additive commutative group, $q$ a natural number and $F \colon K \to X \to Y$ a keyed
function, used in the scheme $\mathrm{Enc}_k(m) = (r, F_k(r) + m)$ with uniform randomness
$r \in X$. For every CPA adversary $A$ with coins in $R$, the CPA advantage of $A$ in the
experiment whose encryption oracle answers at most $q$ queries is at most the PRF advantage of $F$
against the distinguisher built from $A$ plus $q / (2 |X|)$.

This is the reduction of Katz and Lindell, Theorem 3.31, with the sharper statistical term
$q / (2 |X|)$ in place of $q / |X|$.

Formalized by `Cslib.Crypto.PRF.cpaAdvantage_le`, a theorem declared in [CSLibExt/Crypto/SymmetricKey/PRF.lean, line 588](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Crypto/SymmetricKey/PRF.lean#L588). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html#cpa-advantage-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pseudorandom functions](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/cryptography/symmetric-key/pseudorandom-functions)
