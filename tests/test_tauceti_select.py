from trough import tauceti_select


def row(name, doc, kind="theorem", module="TauCeti.A"):
    return {"n": name, "k": kind, "m": module, "d": doc}


def test_a_theorem_is_chosen_when_its_title_names_a_result():
    chosen, _ = tauceti_select.select([
        row("Ex.burnside", "**Burnside's `pᵃqᵇ` theorem**: a finite group ..."),
        row("Ex.jordan", "**The Jordan–Brouwer separation theorem.** ..."),
        row("Ex.schur", "**Schur-Weyl duality for the group ranges:** the commutant ..."),
        row("Ex.serre", "**Serre duality** on a curve. ..."),
        row("Ex.serre2", "**Serre's vanishing theorem.** ..."),
        row("Ex.cellular", "**The cellular approximation theorem.** ..."),
        row("Ex.global", "**Global existence** (Milne VII, Theorem 9.5). For a number field ..."),
        row("Ex.morley", "**Morley's theorem (cardinal form).** ..."),
    ])
    assert chosen == {
        "Ex.burnside": "named theorem", "Ex.cellular": "the theorem", "Ex.global": "cited theorem",
        "Ex.jordan": "named theorem", "Ex.morley": "named theorem", "Ex.schur": "named result",
        "Ex.serre": "named result", "Ex.serre2": "named theorem",
    }


def test_ordinary_lemmas_and_citations_are_not_chosen():
    chosen, _ = tauceti_select.select([
        row("Ex.lemma", "**The coefficient of `tⁿ` in `∏ᵢ (1 + xᵢ t)`**: the sum ..."),
        row("Ex.cited", "**Wedhorn's Lemma 8.34**: exactness in the middle."),
        row("Ex.step", "**Step 3 of Faltings's theorem.** ..."),
        row("Ex.law", "**The Wishart law** of a Gaussian matrix."),
        row("Ex.bare", "**Cauchy estimate** for a disc."),  # no title writes "Cauchy's"
        row("Ex.untitled", "Burnside's theorem, without a bold title."),
        row("Ex.def", "**Burnside's theorem.** As a definition.", kind="instance"),
    ])
    assert chosen == {}


def test_a_definition_carrying_a_theorem_is_chosen_and_a_stated_claim_is_not():
    chosen, assuming = tauceti_select.select([
        row("Ex.yoneda", "**The DG Yoneda lemma.** An equivalence ...", kind="def"),
        row("Ex.AbcConjecture", "**The abc conjecture.** It states ...", kind="def"),
        row("Ex.AbcConjecture.fermat", "**Fermat's theorem from abc.** ...", module="TauCeti.B"),
    ])
    assert chosen == {"Ex.AbcConjecture.fermat": "named theorem", "Ex.yoneda": "theorem as data"}
    assert assuming == {"Ex.AbcConjecture.fermat": {"statement": "Ex.AbcConjecture", "module": "TauCeti.A"}}


def test_the_website_showcase_is_always_chosen():
    name = tauceti_select.SHOWCASE[0]
    chosen, _ = tauceti_select.select([row(name, None)])
    assert chosen == {name: "showcase"}


def test_forms_of_a_result_share_its_key():
    key = tauceti_select.group_key
    assert key("Menger's theorem for adjacent vertices") == key("Menger's theorem, predicate form") == "menger theorem"
    assert key("The Jordan–Brouwer separation theorem") == key("Jordan--Brouwer separation theorem, connected form")
    # A short key without a name keeps its whole head clause.
    assert key("The structure theorem for modules over a PID") != key("The structure theorem for finite abelian groups")
    assert tauceti_select.plain_title("Menger's theorem", "menger theorem")
    assert not tauceti_select.plain_title("Menger's theorem for curves", "menger theorem")
