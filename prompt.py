def lead_instruction(target, preserved_roles):
    """Describe one target without duplicating that identity across the band."""
    return (f"Replace only {target} with the adult in the input portrait. "
            "Use that person's face, hair, build, and outfit in every lead shot. "
            "Keep these people distinct and unchanged: " + "; ".join(preserved_roles)
            + ". Preserve framing and motion as closely as possible. No captions or added performers.")
